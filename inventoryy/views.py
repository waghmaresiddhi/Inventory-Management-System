from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import InventoryItem
from .forms import InventoryItemForm

def dashboard(request):
    inventory_items = InventoryItem.objects.all()
    total_items = inventory_items.count()
    total_quantity = sum(item.quantity for item in inventory_items)
    stock_value = sum(item.quantity * item.unit_price for item in inventory_items)
    recent_activities = ["Added new item", "Updated item quantity", "Deleted an item"]  # Replace with real activities if available
    
    context = {
        'total_items': total_items,
        'total_quantity': total_quantity,
        'stock_value': stock_value,
        'recent_activities': recent_activities,
    }
    return render(request, 'inventoryy/dashboard.html', context)

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_list.html'
    context_object_name = 'inventory_items'

class InventoryCreateView(CreateView):
    model = InventoryItem
    template_name = 'inventoryy/create_inventory.html'
    form_class = InventoryItemForm
    success_url = reverse_lazy('inventory-list')

    def form_valid(self, form):
        return super().form_valid(form)

class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_detail.html'
    context_object_name = 'inventory_item'

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_form.html'
    form_class = InventoryItemForm

    def get_success_url(self):
        return reverse_lazy('inventory_detail', kwargs={'pk': self.object.pk})

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')
