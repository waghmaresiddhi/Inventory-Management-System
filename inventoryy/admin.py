from django.contrib import admin
from .models import Category, InventoryItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Include 'id' if you want to display it

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity', 'unit_price', 'is_active')

admin.site.register(Category, CategoryAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
