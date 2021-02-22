from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
	path('account/<int:pk>/', views.account, name = 'account'),
	path('signup/', SignUpView.as_view(), name = 'signup'),
	
] 

