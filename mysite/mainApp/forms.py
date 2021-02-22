from .models import Registration, Registration2
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class RegistrationForm(ModelForm):
	class Meta:
		model = Registration  # С каким моделью иы работаем
		fields = ['name', 'surname', 'password', 'age', 'date'] # Наши поля

		widgets = {       # Прописмываем харак-ки для каждого отдельного поля
			'name': TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Имя',
				}),
			'surname': TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Фамилия',
				}),	
			'password': TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Пароль',
				}),	
			'age': TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Возраст',
				}),
			'date': DateTimeInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Дата регистрации',
				}),
		}	



# class Registration2Form(forms.ModelForm):
# 	class Meta:
# 		model = Registration2
# 		fields = ['name', 'surname', 'password', 'age', 'date']
