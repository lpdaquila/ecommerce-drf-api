from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Cart
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('addcart/', views.AddCart.as_view(), name='addcart'),
    path('removecart/', views.RemoveCart.as_view(), name='removecart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    # Products
    path('<slug:slug>/', views.ProductDetails.as_view(), name='product_detail'),
    path('', views.ProductList.as_view(), name='product_list'),
]