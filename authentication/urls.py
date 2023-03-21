from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about_us/',about_us,name='about_us'),
    path('contact_us/',contact_us,name='contact_us'),
    path('login/',user_login,name='login'),
    path('register/',user_register,name='register'),
    path('logout/',user_logout,name='logout'),
    path('profile/',profile_setting,name='profile'),
]