from django.db import models
from apps.users.models import Profile, Address

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
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
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