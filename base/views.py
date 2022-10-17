from http.client import HTTPResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class IndexView(TemplateView):
    template_name = "base/pages/index.html"

class RegisterView(TemplateView):
    template_name = "base/pages/register.html"
    
class HeaderView(TemplateView):
    template_name = "base/components/header.html"

class MenuView(TemplateView):
    template_name = "base/components/menu.html"


def register(request):
    if request.method == 'GET':
        return render(request, "base/pages/register.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        return render(request, "base/pages/home.html")
        #user = User.objects.filter('username').first()
        
        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password)

