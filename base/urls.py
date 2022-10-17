from django.http import HttpResponse
from email.header import Header
from django import views
from django.urls import path
from .views import IndexView, HeaderView, register, MenuView

urlpatterns = [
    path('index/', IndexView.as_view()),
    path('header/', HeaderView.as_view()), 
    path('menu/', MenuView.as_view()), 
    #autenticação
    path('register/', register, name = 'register'),
    
]