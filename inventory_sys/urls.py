from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventoryy.urls')),  # Root URL should include 'inventoryy' app URLs
]
