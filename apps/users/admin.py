from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Address, Profile, User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )
    ordering = ("email",)
    search_fields = ("email",)
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login",)}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active",)
        }),
    )
    
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ("user", "name", "email", "phone",)
#     search_fields = ("name", "email", "phone",)
#     list_filter = ("email",)
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "address",
        "number",
        "complement",
        "district",
        "zip_code",
        "city",
        "state",
    )
    search_fields = ("city", "state", "zip_code")
    list_filter = ("state", "city")


