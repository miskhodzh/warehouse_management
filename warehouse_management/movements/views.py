from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ReceiptInvoiceForm
from .models import ReceiptInvoice

class ReceiptInvoiceAdd(FormView):
    template_name = 'warehouse/add.html'
    form_class = ReceiptInvoiceForm
    success_url = reverse_lazy('movements:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ReceiptInvoiceList(ListView):
    template_name = 'movements/list.html'
    model = ReceiptInvoice
    context_object_name = 'products'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
