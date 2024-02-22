from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse, resolve

from .forms import ProductForm, CategoryForm, ProviderForm
from .models import Product, Category, Provider


VIEWS_INFO = {
    'product':{
        'model': Product,
        'form_class': ProductForm,
    },
    'category':{
        'model': Category,
        'form_class': CategoryForm,
    },
    'provider':{
        'model': Provider,
        'form_class': ProviderForm,
    },
}


def object_list(request, entity):
    print(entity)
    template_name = 'list.html'
    model = VIEWS_INFO[entity]['model']
    object_list = model.objects.all()
    headers = model.get_verbose_names()
    context = {
        'object_list': object_list,
        'headers': headers,
        'path': f'/warehouse/{entity}/'
    }
    return render(request, template_name, context)

def object_add(request, entity):
    template_name = 'add.html'

    if request.method == 'POST':
        form = form = VIEWS_INFO[entity]['form_class'](data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(f'warehouse:{entity}_list'))
    else:
        form = form = VIEWS_INFO[entity]['form_class']()
    
    context = {
        'form': form,
    }
    return render(request, template_name, context)
    

def object_edit(request, entity, pk):
    template_name = 'add.html'
    model = VIEWS_INFO[entity]['model']
    object = get_object_or_404(model, pk=pk)
    
    if request.method == 'POST':
        form = VIEWS_INFO[entity]['form_class'](data = request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(f'warehouse:{entity}_list'))
    else:
        form = VIEWS_INFO[entity]['form_class'](instance=object)

    context = {
        'form': form,
    }

    return render(request, template_name, context)

def object_delete(request, entity, pk):
    template_name = 'confirm_delete.html'
    model = VIEWS_INFO[entity]['model']
    object = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        object.delete()
        return redirect(reverse_lazy(f'warehouse:{entity}_list'))

    context = {
        'object': object,
        'undo_url': reverse_lazy(f'warehouse:{entity}_list')
    }    

    return render(request, template_name, context)

class ProductDelete(DeleteView):
    template_name = 'confirm_delete.html'
    model = Product
    success_url = reverse_lazy('warehouse:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.success_url
        return context
