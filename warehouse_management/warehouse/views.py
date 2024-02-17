from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm, CategoryForm, ProviderForm
from .models import Product  


class ProductAdd(FormView):
    template_name = 'warehouse/add.html'
    form_class = ProductForm
    success_url = reverse_lazy('warehouse:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductEdit(UpdateView):
    template_name = 'warehouse/add.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('warehouse:list')


class ProductList(ListView):
    template_name = 'warehouse/list.html'
    model = Product
    context_object_name = 'products'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductDelete(DeleteView):
    template_name = 'warehouse/confirm_delete.html'
    model = Product
    success_url = reverse_lazy('warehouse:list')


class CategoryAdd(FormView):
    template_name = 'warehouse/add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('warehouse:add_category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProviderAdd(FormView):
    template_name = 'warehouse/add.html'
    form_class = ProviderForm
    success_url = reverse_lazy('warehouse:add_provider')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
