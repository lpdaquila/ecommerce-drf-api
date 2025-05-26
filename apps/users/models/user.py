from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return self.email