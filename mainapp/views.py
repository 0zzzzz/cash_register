import datetime

from django.http import Http404, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.models import Item
from mainapp.serializers import ItemSerializer
from mainapp.services.pdf_service import create_pdf


class ItemCreateAPIView(APIView):
    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemUpdateAPIView(APIView):
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
    def post(self, request):
        items_pk = None
        if 'items' in request.data:
            items_pk = request.data['items']
        items = Item.objects.filter(pk__in=items_pk)
        data = {
            'items': items,
        }
        date = datetime.datetime.now()
        pdf_name = f'receipt_{date.strftime("%A_%d_%B_%Y_%I:%M%p_%s")}'
        create_pdf(data, 'pdf/receipt.html', pdf_name)
        # html_response = create_pdf(data, 'pdf/receipt.html', f'receipt')
        html_respons1 = 'hi'
        return HttpResponse(html_respons1, content_type='application/pdf')
