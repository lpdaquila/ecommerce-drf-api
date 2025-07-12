"""
URL configuration for project project.

Nested endpoints of "Users" and "Orders" apps
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.users.urls')),
    # path('api/v1/order/', include('apps.orders.urls')),
    path('api/v1/', include('apps.products.urls')),
] 