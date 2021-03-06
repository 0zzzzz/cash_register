import datetime
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.models import Item
from mainapp.serializers import ItemSerializer
from mainapp.services.pdf_service import create_pdf
import qrcode


class ItemCreateAPIView(APIView):
    """Создание товара"""

    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemUpdateAPIView(APIView):
    """Изменение товара"""
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReceiptPDFRender(APIView):
    """Создание чека в фомате PDF"""

    def post(self, request):
        items_pk = None
        if 'items' in request.data:
            items_pk = request.data['items']
        items = Item.objects.filter(pk__in=items_pk)
        # по хорошему необходимо создать дополнительные модели для кассового чека
        # и поместить подобную функцию туда
        items_total_price = 0
        for item in items:
            items_total_price += item.item_cost

        date = datetime.datetime.now()
        data = {
            'items': items,
            'date': date.strftime('%m.%d.%y %H:%M'),
            'items_total_price': items_total_price,
        }
        pdf_name = f'receipt_{date.strftime("%A_%d_%B_%Y_%I_%M%p_%s")}'
        create_pdf(data, 'pdf/receipt.html', pdf_name)
        image = qrcode.make(f'{request.get_host()}/media/pdf/{pdf_name}.pdf')
        image.save('media/temp_qr/temp_qr_file.png')
        with open('media/temp_qr/temp_qr_file.png', 'rb') as image:
            return HttpResponse(image, content_type='image/png')
