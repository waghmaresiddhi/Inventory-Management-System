# inventoryy/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import InventoryItem
from django.urls import reverse_lazy

def dashboard(request):
    return render(request, 'inventoryy/dashboard.html')

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_list.html'
    context_object_name = 'inventory_items'

class InventoryCreateView(CreateView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_form.html'
    fields = '__all__'  # or specify fields explicitly
    success_url = reverse_lazy('inventory-list')

class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_detail.html'
    context_object_name = 'inventory_item'

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_form.html'
    fields = '__all__'  # or specify fields explicitly

    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.pk})

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory-list')
