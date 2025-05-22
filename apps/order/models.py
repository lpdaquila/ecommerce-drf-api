from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    """
    Order:
            user - FK User
            total - Float
            status - Choices
                ('A', 'Approved'),
                ('C', 'Created'),
                ('R', 'Refused'),
                ('P', 'Pending'),
                ('S', 'Send'),
                ('F', 'Finished'),
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        max_length=1,
        choices=(
            ('A', 'Approved'),
            ('C', 'Created'),
            ('R', 'Refused'),
            ('P', 'Pending'),
            ('S', 'Send'),
            ('F', 'Finished'),
        ),
        default='C'
    )
    
    def __str__(self) -> str:
        return f'Order {self.pk}'

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
