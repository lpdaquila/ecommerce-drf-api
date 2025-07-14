from django.urls import path
from . import views

apps_name = 'products'

urlpatterns = [
    path('products/', views.Products.as_view(), name='products'),
    path('product/<str:slug>', views.ProductDetail.as_view(), name='product_detail'),
]