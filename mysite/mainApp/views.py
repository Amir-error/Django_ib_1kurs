from django.shortcuts import render, redirect
from .models import Registration, Registration2
from .forms import RegistrationForm

# Create your views here.
def index(request):
	data = {
		'title' : 'Главная стр!!!!',
		'sto_num': 'wktieht' ,
		'obj': {
					'car': 'BMW',
					'age': '18',
					'hobby': 'programmist'	
				}
	}
	return render(request, 'mainApp/homePage.html', data)
	

def about(request):
	return render(request, 'mainApp/aboutMe.html')

def contact(request):
	return render(request, 'mainApp/ourContact.html')	
#НЕ СМОРТИТЕ НЕ НУЖНО
def registration(request):    # Регистрация вместе с проверкой на #
	check_name = True
	error = ''
	##############################################
	# b = Registration.objects.filter(name__startswith = 'Ами') # совпадение нач букв
	# spis = [e.name for e in Registration.objects.all() if True]
	# a = Registration.objects.get( id = 19 )
	# b = a.difference_time()
	###############################################	
	if request.method == 'POST':
		form = RegistrationForm(request.POST)  #
		a = form.data.get("name")
		if form.is_valid():
			for e in Registration.objects.all():
				if a != e.name:
					continue
				else:
					error = "Имя уже занято"
					check_name = False
					break
			if check_name:
				form.save()
						
		else:
			error = 'Форма была неверной'	

	form = RegistrationForm()
	data = {
		'form': form ,
		'error': error ,
		
		
	}
	return render(request, 'mainApp/registration.html', data)		
	
	
			
#НЕ СМОРТИТЕ НЕ НУЖНО
def registration2(request):    # Регистрация вместе с проверкой на идентичность
	error = ''
	check_name = True
	#z = Registration2.objects.get(id = 12)
	if request.method == 'POST':
		for obj in Registration2.objects.all():
			if request.POST['name'] == obj.name:
				error = 'Имя уже занято'
				check_name = False
				break
			else:
				continue
		if check_name:	
			b = Registration2(name = request.POST['name'],  surname = request.POST['surname'], password = request.POST['password'], age = request.POST['age'], date = Registration.time_now())
			b.save()
			error = 'Регистрация успешна выполнена'	
					
	data = {
		'error': error ,
		#'z': z ,
		
	}

	return render(request, 'mainApp/registration2.html', data)
#НЕ СМОРТИТЕ НЕ НУЖНО
def authorization(request):
	error = ''
	if request.method == 'POST':
		
		for obj in Registration2.objects.all():
			if (request.POST['name'] == obj.name) and (request.POST['password'] == obj.password):
				return redirect('mainApp:home')
			else:
				continue
		error = 'Логин и пароль введены не коректно'					
				
	data = {
		'error': error ,
	}	
		
	return render(request, 'mainApp/authorization.html', data)		
			
	
			

					
			

	
		
		

		
	
	
	


	
		
					
		
		
		

		





	


			

