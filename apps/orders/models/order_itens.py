from django.db import models
from apps.users.models.user import User

from apps.orders.models.order import Order

class OrderItem(models.Model):
    """
    OrderItem:
                order - FK Order
                product - Char
                product_id - Int
                variation - Char
                variation_id - Int
                price - Float
                promotional_price - Float
                quantity - Int
                image - Char
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=50)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0.0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(
        max_length=2000, 
        blank=True, 
        null=True
    ) #TODO: remove blank and null for production
    
    def __str__(self) -> str:
        return f'Item of Order {self.order.pk} - {self.product}'