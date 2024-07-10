from django.contrib import admin
from django.db import models  # Import models from Django's database module
from .models import InventoryItem

class InventoryItemAdmin(admin.ModelAdmin):
    # Define fields to display in the admin list view
    list_display = ['name', 'quantity', 'unit_price', 'manufacture_date', 'purchase_date', 'supplier', 'location']

    # Customize the form fieldsets
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'quantity', 'unit_price')
        }),
        ('Date Information', {
            'fields': ('manufacture_date', 'purchase_date'),
            'classes': ('collapse',)  # Collapsible section
        }),
        ('Additional Information', {
            'fields': ('supplier', 'location', 'activity_status'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )

    # Adjust the form field widgets
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextInputWidget(attrs={'size':'60'})},  # Adjust size as needed
    }

# Register your models with the custom admin class
admin.site.register(InventoryItem, InventoryItemAdmin)
