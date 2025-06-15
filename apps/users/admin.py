from django.contrib import admin

from .models.profile import Profile
from .models.address import Address

admin.site.register(Profile)
admin.site.register(Address)


