from datetime import date
from django.db import models
from django.forms import ValidationError
from apps.users.models.users import User

from apps.utils import validate_cpf

class Profile(models.Model):
    """
    ### UserProfile	
            user - FK User (or OneToOne)
            name - Char
            email - Email
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    document = models.CharField(max_length=11, null=True, blank=True, unique=True)
    
    # @property
    # def age(self):
    #     today = date.today()
    #     age = today.year - self.birth_date.year - \
    #         ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    #     return age
    
    def clean(self):
        if self.document:
            if not validate_cpf(self.document):
                raise ValidationError("Invalid Document")
            

    def __str__(self):
        return self.name or "Guest Profile"
        # return f'{self.user.first_name} {self.user.last_name}'


