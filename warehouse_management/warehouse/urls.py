from django.urls import path

from .views import product_list, add

app_name = 'warehouse'
urlpatterns = [
    path('list/', product_list, name='list'),
    path('add/', add, name='add'),
]
