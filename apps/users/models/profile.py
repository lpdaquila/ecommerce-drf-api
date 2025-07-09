import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models
from apps.users.models.users import User

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


