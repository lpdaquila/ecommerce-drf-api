from django.urls import path
from . import views

apps_name = 'user'

urlpatterns = [
    path('update/', views.UpdateProfile.as_view(), name='update'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('get_user/', views.GetUser.as_view(), name='get_user'),
    path('profile/', views.CreateProfile.as_view(), name='create'),
]