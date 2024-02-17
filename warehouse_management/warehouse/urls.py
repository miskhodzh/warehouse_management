from django.urls import path

from .views import ProductAdd, ProductList, CategoryAdd, ProviderAdd, ProductEdit, ProductDelete

app_name = 'warehouse'
urlpatterns = [
    path('list/', ProductList.as_view(), name='list'),
    path('product/add/', ProductAdd.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', ProductEdit.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='delete_product'),
    path('category/add/', CategoryAdd.as_view(), name='add_category'),
    path('provider/add/', ProviderAdd.as_view(), name='add_provider'),
]
