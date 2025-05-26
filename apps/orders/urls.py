from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('payment/', views.Payment.as_view(), name='payment'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('details/<int:pk>/', views.Details.as_view(), name='details'),
]