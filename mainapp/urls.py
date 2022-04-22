from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mainapp import views as api

app_name = 'mainapp'

urlpatterns = [
    path('item_create/', api.ItemCreateAPIView.as_view(), name='item_create'),
    path('item_update/<int:pk>/', api.ItemUpdateAPIView.as_view(), name='item_update'),
    path('cash_machine/', api.ReceiptPDFRender.as_view(), name='receipt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
