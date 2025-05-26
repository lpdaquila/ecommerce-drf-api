from django.urls import path
from . import views

apps_name = 'profile'

urlpatterns = [
    path('update/', views.UpdateProfile.as_view(), name='update'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('', views.CreateProfile.as_view(), name='create'),
]