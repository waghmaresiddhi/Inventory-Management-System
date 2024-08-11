from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'unit_price', 'manufacture_date', 'purchase_date', 'supplier', 'location', 'activity_status', 'minimum_stock_level']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'manufacture_date': forms.DateInput(attrs={'type': 'date'}),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'unit_price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
        }

class InventorySearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))
    category = forms.CharField(required=False, label='Category', widget=forms.TextInput(attrs={'placeholder': 'Category', 'class': 'form-control'}))
    supplier = forms.CharField(required=False, label='Supplier', widget=forms.TextInput(attrs={'placeholder': 'Supplier', 'class': 'form-control'}))
    location = forms.CharField(required=False, label='Location', widget=forms.TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}))
    status = forms.ChoiceField(required=False, label='Status', choices=[('', 'All'), ('active', 'Active'), ('inactive', 'Inactive')], widget=forms.Select(attrs={'class': 'form-control'}))
    date_range_start = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_range_end = forms.DateField(required=False, label='End Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    sort_by = forms.ChoiceField(required=False, label='Sort By', choices=[('', 'None'), ('name', 'Name'), ('quantity', 'Quantity'), ('unit_price', 'Unit Price')], widget=forms.Select(attrs={'class': 'form-control'}))
