from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

class User(AbstractBaseUser):
    """
    User
        name - Char
        email - EmailField
        staff - Bool
    """
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
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