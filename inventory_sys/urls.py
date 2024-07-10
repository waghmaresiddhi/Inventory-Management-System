# urls.py (project level)

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventoryy.urls')),  # Include app-level URLs
]
