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