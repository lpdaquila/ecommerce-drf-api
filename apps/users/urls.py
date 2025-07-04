from django.urls import path
from . import views

apps_name = 'user'

urlpatterns = [
    # path('update/', views.UpdateProfile.as_view(), name='update'),
    path('login/', views.Login.as_view(), name='login'),
    path('create_account/', views.CreateAccount.as_view(), name='create_account'),
    path('get_user/', views.GetUser.as_view(), name='get_user'),
    # path('profile/', views.CreateProfile.as_view(), name='create'),
]