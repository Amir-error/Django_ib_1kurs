from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
	path('', views.index, name = "home"),
	path('about/', views.about, name = "about"),
	path('contact/', views.contact, name = "contact"),
	path('registration/', views.registration, name = 'registration'),
	path('registration2/', views.registration2, name = 'registration2'),
	path('authorization/', views.authorization, name = 'authorization'),
	
]	


