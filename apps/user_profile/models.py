from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re 
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
        return self.user.username
        # return f'{self.user.first_name} {self.user.last_name}'

class UserAddress(models.Model):
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
            state - Choices
                ('AC', 'Acre'),
                ('AL', 'Alagoas'),
                ('AP', 'Amapá'),
                ('AM', 'Amazonas'),
                ('BA', 'Bahia'),
                ('CE', 'Ceará'),
                ('DF', 'Distrito Federal'),
                ('ES', 'Espírito Santo'),
                ('GO', 'Goiás'),
                ('MA', 'Maranhão'),
                ('MT', 'Mato Grosso'),
                ('MS', 'Mato Grosso do Sul'),
                ('MG', 'Minas Gerais'),
                ('PA', 'Pará'),
                ('PB', 'Paraíba'),
                ('PR', 'Paraná'),
                ('PE', 'Pernambuco'),
                ('PI', 'Piauí'),
                ('RJ', 'Rio de Janeiro'),
                ('RN', 'Rio Grande do Norte'),
                ('RS', 'Rio Grande do Sul'),
                ('RO', 'Rondônia'),
                ('RR', 'Roraima'),
                ('SC', 'Santa Catarina'),
                ('SP', 'São Paulo'),
                ('SE', 'Sergipe'),
                ('TO', 'Tocantins'),
    """
        
    address_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=2,
        choices=[
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins')
        ]
    )
    
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
