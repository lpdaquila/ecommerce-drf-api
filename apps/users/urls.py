from django.urls import path
from . import views

apps_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('create_account/', views.CreateAccountView.as_view(), name='create_account'),
    path('user/', views.GetUserView.as_view(), name='user'),
    path('refresh/', views.TokenRefreshView.as_view(), name='refresh'),
    path('profile/<int:profile_id>', views.ProfileDetailView.as_view(), name='profile_detail'),
]