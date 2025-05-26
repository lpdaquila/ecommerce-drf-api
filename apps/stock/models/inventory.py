from django.db import models
from apps.products.models.product import Variation

class Stock(models.Model):
    """
    Stock:
        variation - FK Variation
        quantity - Int
        min_quantity - Int
        max_quantity - Int
    """
    variation = models.ForeignKey(
        Variation, 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    min_quantity = models.PositiveIntegerField()
    max_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.variation.name} - {self.quantity}'