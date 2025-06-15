from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, 
    BaseUserManager, Permission)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    """
    User
        name - Char
        email - Email
        document - Char
        data_joined - DateTime
        is_active - True
        is_staff - Bool
    """
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    document = models.CharField(max_length=11, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'document']
    
    def __str__(self) -> str:
        return self.email
    
class Group(models.Model):
    """
    Group
        name - Char
    """
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class GroupPermissions(models.Model):
    """
    GroupPermissions
        group - FK Group
        permission - FK Permission
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('group', 'permission')
    
    def __str__(self) -> str:
        return f"{self.group.name} - {self.permission.name}"
    
class UserGroups(models.Model):
    """
    UserGroups
        user - FK User
        group - FK Group
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'group')
    
    def __str__(self) -> str:
        return f"{self.user.email} - {self.group.name}"