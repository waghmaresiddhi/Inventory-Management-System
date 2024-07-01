from django.contrib import admin
from .models import Category, InventoryItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display 'id' and 'name' fields in the admin list view

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity', 'unit_price', 'is_active')  # Display these fields in the admin list view

admin.site.register(Category, CategoryAdmin)  # Register Category model with the custom admin configuration
admin.site.register(InventoryItem, InventoryItemAdmin)  # Register InventoryItem model with the custom admin configuration
