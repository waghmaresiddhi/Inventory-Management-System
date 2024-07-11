from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import InventoryItem
from .forms import InventoryItemForm
import calendar

def dashboard(request):
    inventory_items = InventoryItem.objects.all()
    total_items = inventory_items.count()
    total_quantity = sum(item.quantity for item in inventory_items)
    stock_value = sum(item.quantity * item.unit_price for item in inventory_items)
    recent_activities = ["Added new item", "Updated item quantity", "Deleted an item"]

    # Initialize a dictionary for all months
    monthly_data = {month: 0 for month in calendar.month_name[1:]}

    # Group data by month for the chart
    inventory_by_month = (
        inventory_items
        .extra(select={'month': "strftime('%%m', purchase_date)"})
        .values('month')
        .annotate(total=Count('id'))  # Count the number of items
        .order_by('month')
    )

    # Update monthly data with actual values
    for item in inventory_by_month:
        month_name = calendar.month_name[int(item['month'])]
        monthly_data[month_name] = item['total']

    chart_data = {
        'labels': list(monthly_data.keys()),
        'data': list(monthly_data.values()),
    }
    
    context = {
        'total_items': total_items,
        'stock_value': stock_value,
        'recent_activities': recent_activities,
        'chart_data': chart_data,
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

class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_detail.html'
    context_object_name = 'inventory_item'

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_update.html'
    form_class = InventoryItemForm

    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.pk})

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory-list')
