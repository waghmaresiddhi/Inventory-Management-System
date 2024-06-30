from django.http import HttpResponse
from .models import InventoryItem

def index(request):
    # Retrieve all InventoryItem instances from the database
    inventory_items = InventoryItem.objects.all()

    # Prepare a response to display all inventory items
    output = ', '.join(item.name for item in inventory_items)
    return HttpResponse(output)
