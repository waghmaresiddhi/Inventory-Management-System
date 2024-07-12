from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'unit_price', 'manufacture_date', 'purchase_date', 'supplier', 'location', 'activity_status', 'minimum_stock_level']  # Include the new field

class InventorySearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    category = forms.CharField(required=False, label='Category', widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    supplier = forms.CharField(required=False, label='Supplier', widget=forms.TextInput(attrs={'placeholder': 'Supplier'}))
    location = forms.CharField(required=False, label='Location', widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    status = forms.ChoiceField(required=False, label='Status', choices=[('', 'All'), ('active', 'Active'), ('inactive', 'Inactive')])
    date_range_start = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    date_range_end = forms.DateField(required=False, label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
    sort_by = forms.ChoiceField(required=False, label='Sort By', choices=[('', 'None'), ('name', 'Name'), ('quantity', 'Quantity'), ('unit_price', 'Unit Price')])
