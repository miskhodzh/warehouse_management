from django.urls import path

from .views import ReceiptInvoiceAdd, ReceiptInvoiceList

app_name = 'movements'
urlpatterns = [
    path('add/', ReceiptInvoiceAdd.as_view(), name='add'),
    path('list/', ReceiptInvoiceList.as_view(), name='list'),
]
