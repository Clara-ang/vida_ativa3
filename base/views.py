from pipes import Template
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "base/pages/index.html"

class RegisterView(TemplateView):
    template_name = "base/pages/register.html"
    
class HeaderView(TemplateView):
    template_name = "base/pages/header.html"


#def register(request):
   # if request.method == 'GET':
   #     return render (request, 'base/pages/register.html')
   # else :
   #    username = request.post.get('username')
   #    email = request.post.get('email')
   #  password = request.post.get('password')

   # user = User.objects.create_user(username=username, email=email, password=password)
   #     return render(request, 'base/pages/index.html')

# Create your views here.
