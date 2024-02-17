from django.forms import ModelForm
from .models import ReceiptInvoice

class ReceiptInvoiceForm(ModelForm):
    class Meta:
        model = ReceiptInvoice
        fields = '__all__'