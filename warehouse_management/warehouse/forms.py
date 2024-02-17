from django.forms import ModelForm

from .models import Product, Category, Provider


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ('__all__')

