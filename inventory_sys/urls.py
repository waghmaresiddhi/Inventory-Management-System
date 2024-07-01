from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory_management/', include('inventoryy.urls')),
    # Add other URL patterns as needed
]
