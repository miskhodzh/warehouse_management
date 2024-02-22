from django.urls import path

from .views import object_list, object_edit, object_add, object_delete

app_name = 'warehouse'
urlpatterns = [
    path('product/list/', object_list, {'entity': 'product'}, name='product_list'),
    path('category/list/', object_list, {'entity': 'category'}, name='category_list'),
    path('provider/list/', object_list, {'entity': 'provider'}, name='provider_list'),
    path('product/add/', object_add, {'entity': 'product'}, name='add_product'),
    path('category/add/', object_add, {'entity': 'category'}, name='add_category'),
    path('provider/add/', object_add, {'entity': 'provider'}, name='add_provider'),
    path('product/<int:pk>/edit/', object_edit, {'entity': 'product'}, name='edit_product'),
    path('category/<int:pk>/edit/', object_edit, {'entity': 'category'}, name='edit_category'),
    path('provider/<int:pk>/edit/', object_edit, {'entity': 'provider'}, name='edit_provider'),
    path('product/<int:pk>/delete/', object_delete, {'entity': 'product'}, name='delete_product'),
    path('category/<int:pk>/delete/', object_delete, {'entity': 'category'}, name='delete_category'),
    path('provider/<int:pk>/delete/', object_delete, {'entity': 'provider'}, name='delete_provider'),
]
