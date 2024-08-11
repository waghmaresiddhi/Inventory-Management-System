from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateField()
    purchase_date = models.DateField()
    supplier = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    activity_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    minimum_stock_level = models.IntegerField(default=0)  # New field for minimum stock level

    def __str__(self):
        return self.name

    def check_stock(self):
        if self.quantity < self.minimum_stock_level:
            return True
        return False