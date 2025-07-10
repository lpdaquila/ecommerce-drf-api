import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, 
    BaseUserManager)

##### User

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    User
        name - Char
        data_joined - DateTime
        is_active - True
        is_staff - Bool
    """
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self) -> str:
        return self.email
    
##### Profile

class Profile(models.Model):
    """
    ### Profile	
            user - FK (OneToOne) User
            name - FK User name
            email - FK User email
            phone - Char
            document - Char
            date_joined - Date
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.CharField(max_length=14, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    
    # @property
    # def age(self):
    #     today = date.today()
    #     age = today.year - self.birth_date.year - \
    #         ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    #     return age
            
    def __str__(self):
        return self.user.name
    
class AnonymousProfile(models.Model):
    """
        ### Anonymous Profile
                name - Char
                email -Email
                public_id - UUID
                expires_at - Date
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    public_id = models.UUIDField(unique=True)
    expires_at = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
        
    def is_valid_token(self) -> bool | None:
        return timezone.now() < self.expires_at if self.expires_at else None
    
    def renew_token(self, hours: int = 48):
        self.public_id = uuid.uuid4()
        self.expires_at = timezone.now() + timedelta(hours=hours)
        self.save()
        
###### Address

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

    def __str__(self):
        return f'{self.address}, {self.number} - {self.city}/{self.state}'