from django.urls import path
from .views import *

urlpatterns = [
    path('',payment_page,name='payment' ),
    path('success/',success_page,name='success' ),
]