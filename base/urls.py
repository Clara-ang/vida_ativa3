from django.urls import path
from .views import IndexView, HeaderView, RegisterView

urlpatterns = [
    path('index/', IndexView.as_view()),
    path('register/', RegisterView.as_view()),
    path('header/', HeaderView.as_view()),  
    #autenticação
    #path('cadastro/',nomeview.as.view(), name='register' )
]