from django.db import models
from apps.products.models.product import Product, Variation

class Stock(models.Model):
    """
    Stock:
        product - FK Product
        variation - FK Variation
        quantity - Int
        min_quantity - Int
        max_quantity - Int
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(
        Variation, 
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    min_quantity = models.PositiveIntegerField()
    max_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'