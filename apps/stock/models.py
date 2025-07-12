from django.db import models
from apps.products.models import ProductVariant

class Inventory(models.Model):
    product_var = models.OneToOneField(ProductVariant, on_delete=models.CASCADE)
    # stock_type = models.ForeignKey('StockType', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    # max_quantity = models.PositiveIntegerField()
    # min_quantity = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.product_var.product.name} - {self.quantity}'
    
# class StockType(models.Model):
#     name = models.CharField(max_length=100)
    