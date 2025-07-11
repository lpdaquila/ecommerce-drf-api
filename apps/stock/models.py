from django.db import models
from apps.products.models import ProductVariant

class Inventory(models.Model):
    product_var = models.OneToOneField(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    max_quantity = models.PositiveIntegerField()
    min_quantity = models.PositiveIntegerField()