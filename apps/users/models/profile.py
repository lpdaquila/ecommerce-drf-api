import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from apps.users.models.users import User

from apps.utils import validate_cpf

class Profile(models.Model):
    """
    ### Profile	
            user - FK (OneToOne) User
            name - Char
            email - Email
            phone - Char
            document - Char
            date_joined - Date
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    # Guest Data
    guest_name = models.CharField(max_length=100, null=True)
    guest_email = models.EmailField(null=True, unique=True)
    guest_public_id = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        null=True, 
        blank=True,
        unique=True
    )
    guest_public_id_expires_at = models.DateTimeField(
        default=lambda: timezone.now() + timedelta(hours=48),
        null=True,
        blank=True
    )
    
    # User Data
    document = models.CharField(max_length=14, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    
    @property
    def email(self):
        return self.user.email if self.user else self.guest_email
    
    @property
    def is_guest(self) -> bool:
        return self.user is None
    
    def is_valid_token(self) -> bool | None:
        return timezone.now() < self.guest_public_id_expires_at if self.guest_public_id_expires_at else None
    
    def renew_token(self, hours: int = 48):
        self.guest_public_id = uuid.uuid4()
        self.guest_public_id_expires_at = timezone.now() + timedelta(hours=hours)
        self.save()
    
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
        return self.user.name if self.user else "Guest Profile"


