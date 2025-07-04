"""
URL configuration for project project.

Nested endpoints of "Users" and "Orders" apps
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.users.urls')),
    # path('api/order/', include('apps.orders.urls')),
    # path('', include('apps.products.urls')),
] 