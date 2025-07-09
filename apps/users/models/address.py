import re 
from django.db import models
from django.forms import ValidationError
from apps.users.models import Profile


class Address(models.Model):
    """
    UserAddress:
            address_name - char
            user - FK User
            address - char
            number - char
            complement - char
            district - char
            zip_code - Char
            city - char
            state - Char
    """
        
    address_name = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    
    class Meta:
        # Need to add verbose_name and verbose_name_plural
        # to make the admin interface more user-friendly
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
        
    def clean(self):
        error_messages = {}
        
        if not re.match(r'^\d{5}-\d{3}$', self.zip_code):
            error_messages['zip_code'] = 'Invalid ZIP code format. Use XXXXX-XXX.'
            
        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return f'{self.address}, {self.number} - {self.city}/{self.state}'