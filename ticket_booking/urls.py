from django.urls import path
from .views import *

urlpatterns = [
    path('',search_page,name='search'),
    path('book/',book_page,name='book'),
    path('train-info/',train_info,name='train_info'),
    path('dashboard/',dashboard,name='dashboard'),
    path('<int:id>',book_train,name='book-train'),
    path('routes/',show_routes,name='routes'),
]