from django.urls import path
from . import views

apps_name = 'user'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('create_account/', views.CreateAccount.as_view(), name='create_account'),
    path('get_user/', views.GetUser.as_view(), name='get_user'),
    path('refresh/', views.TokenRefreshView.as_view(), name='refresh'),
]