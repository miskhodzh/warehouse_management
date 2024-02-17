from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('move/', include('movements.urls')),
    path('warehouse/', include('warehouse.urls')),
]
