from datetime import date
from django.db import models
from django.forms import ValidationError
from apps.users.models.user import User

from apps.utils import validate_cpf

class UserProfile(models.Model):
    """
    UserProfile	
            user - FK User (or OneToOne)
            age - Int
            birth_date - Date
            identity - char
            addresses - FK UserAddress
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    document = models.CharField(max_length=11)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - \
            ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    def clean(self):
        error_messages = {}
        
        if not validate_cpf(self.document):
            error_messages['document'] = 'Invalid CPF'
            
        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return self.user.email
        # return f'{self.user.first_name} {self.user.last_name}'


