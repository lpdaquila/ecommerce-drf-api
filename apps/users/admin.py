from django.contrib import admin

from .models.profile import UserProfile
from .models.address import UserAddress

admin.site.register(UserProfile)
admin.site.register(UserAddress)


