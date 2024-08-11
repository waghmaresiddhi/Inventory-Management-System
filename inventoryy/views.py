from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.postgres.search import SearchVector
from .models import InventoryItem
from .forms import InventoryItemForm, InventorySearchForm
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

    # Check if the request is for low stock items
    show_low_stock = request.GET.get('show_low_stock', 'false') == 'true'

    low_stock_items = []
    if show_low_stock:
        low_stock_items = inventory_items.filter(quantity__lt=F('minimum_stock_level'))

        # Optional: Send email notifications for low stock items
        if low_stock_items.exists():
            send_low_stock_notification(low_stock_items)

    context = {
        'total_items': total_items,
        'stock_value': stock_value,
        'recent_activities': recent_activities,
        'chart_data': chart_data,
        'low_stock_items': low_stock_items,  # Add to context to display on dashboard
        'show_low_stock': show_low_stock,   # Track if the low stock view is active
    }
    return render(request, 'inventoryy/dashboard.html', context)

def send_low_stock_notification(items):
    for item in items:
        send_mail(
            'Low Stock Alert',
            f'The stock for {item.name} is below the minimum level. Current stock: {item.quantity}.',
            'your_email@example.com',  # Sender's email address
            ['admin@example.com'],    # Recipient email address(es)
            fail_silently=False,
        )

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_list.html'
    context_object_name = 'inventory_items'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InventorySearchForm(self.request.GET)
        return context

class InventoryCreateView(CreateView):
    model = InventoryItem
    template_name = 'inventoryy/create_inventory.html'
    form_class = InventoryItemForm
    success_url = reverse_lazy('inventory-list')

class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventoryy/inventory_detail.html'
    context_object_name = 'item'

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    template_name = 'inventoryy/edit_inventory_item.html'
    form_class = InventoryItemForm

    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.pk})

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventoryy/delete_inventory_item.html'
    success_url = reverse_lazy('inventory-list')
