# views.py
from django.shortcuts import render
from .models import InventoryItem

def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventoryy/inventory_list.html', {'items': items})
