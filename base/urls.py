from django.urls import path
from .views import IndexView, HeaderView, LoginView

urlpatterns = [
    path('index/', IndexView.as_view()),
    path('login/', LoginView.as_view()),
    path('header/', HeaderView.as_view()),  
]