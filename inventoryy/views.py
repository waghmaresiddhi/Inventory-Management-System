from django.shortcuts import render
from django.views.generic import ListView
from .models import InventoryItem

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_list.html'
    context_object_name = 'inventory_items'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return InventoryItem.objects.filter(name__icontains=query)
        return InventoryItem.objects.all()
