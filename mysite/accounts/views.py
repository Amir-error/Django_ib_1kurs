from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AuthUserForm
from news.models import Articles                                              
from django.http import Http404

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
# Create your views here.

#Регистрация
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('mainApp:home')
    template_name = 'signup.html'

#Авторизация
class LoginUpView(LoginView):
	template_name = 'login.html'
	form_class = AuthUserForm  
	success_url = reverse_lazy('mainApp:home')


# Аккаунт
def account(request, pk):
	try:
		access = False
		our_articles_list = Articles.objects.filter(id_user = pk)	
		if request.user.id == pk:
			access = True
	except:
		raise Http404("404")	
	data = {
		'our_articles_list': our_articles_list , 
		'access': access ,
	}

	return render(request, 'accounts.html', data)
		
	
