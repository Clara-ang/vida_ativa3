from pipes import Template
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "base/pages/index.html"

class LoginView(TemplateView):
    template_name = "base/pages/login.html"
    
class HeaderView(TemplateView):
    template_name = "base/pages/header.html"



# Create your views here.
