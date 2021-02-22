from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AuthUserForm(forms.ModelForm, AuthenticationForm):
	class Meta:
		model = User
		fields = ['username', 'password']