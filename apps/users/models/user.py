from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return self.email
    
class Group(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class GroupPermissions(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('group', 'permission')
    
    def __str__(self) -> str:
        return f"{self.group.name} - {self.permission.name}"
    
class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'group')
    
    def __str__(self) -> str:
        return f"{self.user.email} - {self.group.name}"