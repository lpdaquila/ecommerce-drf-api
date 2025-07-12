from django.urls import path
from . import views

apps_name = 'products'

urlpatterns = [
    path('', views.Products.as_view(), name='products'),
]