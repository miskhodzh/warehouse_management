from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('main/', include('movements.urls')),
    path('warehous', include('warehouse.urls')),
]
