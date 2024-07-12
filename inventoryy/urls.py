from django.urls import path
from .views import (
    InventoryListView,
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView,
    InventoryDetailView,
    dashboard,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/add/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory-edit'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    # other URL patterns
]
