from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .forms import ProductForm, CategoryForm, ProviderForm
from .models import Product  


class ProductAdd(FormView):
    template_name = 'add.html'
    form_class = ProductForm
    success_url = reverse_lazy('warehouse:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductEdit(UpdateView):
    template_name = 'add.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('warehouse:list')


class ProductList(ListView):
    template_name = 'list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Дополнительные данные, которые вы хотите передать в шаблон
        context['headers'] = [
            'Код товара',
            'Название',
            'Категория',
            'Описание',
            'Кол-во',
            'Поставщик',
            'Действия'
        ]
        context['path'] = '/warehouse/product/'
        return context
    

class ProductDelete(DeleteView):
    template_name = 'confirm_delete.html'
    model = Product
    success_url = reverse_lazy('warehouse:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.success_url
        return context


class CategoryAdd(FormView):
    template_name = 'add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('warehouse:add_category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProviderAdd(FormView):
    template_name = 'add.html'
    form_class = ProviderForm
    success_url = reverse_lazy('warehouse:add_provider')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
