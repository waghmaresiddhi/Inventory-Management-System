from django.urls import path
from .views import dashboard, InventoryListView, InventoryCreateView, InventoryDetailView, InventoryUpdateView, InventoryDeleteView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/add/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory-edit'),  # Ensure this line is correctly set
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
]
