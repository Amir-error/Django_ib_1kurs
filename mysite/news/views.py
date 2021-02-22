from django.shortcuts import render, redirect # (redirect- функция переадрисации)
from .models import Articles 

from django.http import Http404, HttpResponseRedirect
from django.utils import timezone

# Create your views here.
#Все новости
def news_home(request):   # Новости
	search_news_list = []
	error = ""
	if request.method == 'POST':  # реагирует на POST запрос
		search_news_list = Articles.objects.filter(title__startswith = request.POST['news']) # Поиск новостей
		search_news_list = search_news_list.order_by('date')	
		if len(search_news_list) == 0:
			error = "По вашему запросу ничего не найдено"
		
	length = len(search_news_list)	
	object_all = Articles.objects.all()
	articles_list = Articles.objects.order_by('-date')
	
	

	data = {
		'articles_list': articles_list ,
		'length': length ,
		'z': request.user ,
		'search_news_list': search_news_list ,
		'error': error ,
	}

	return render(request, 'news/news_home.html', data)
#просмотр отдельной статьи
def detailview(request, articles_id):
	try:
		a = Articles.objects.get(id = articles_id)
	except:
		raise Http404("Статья не найдена")
	data = {
		"article": a ,
	}	

	return render(request, 'news/detailview.html', data)
# Редактирование статьи
def redaction(request, articles_id2, articles_id):   # Редактирование  \/  Использование 2 динамических параметров URL / ЧАНДА
	obj = Articles.objects.get(id = articles_id2)
	if request.method == 'POST':
		obj.title = request.POST['title']
		obj.anons = request.POST['anons']
		obj.full_text = request.POST['full_text']
		obj.date = timezone.datetime.now()
		obj.save()
		return redirect('news:news_home')
	data = {
		'obj': obj ,
	}
	
	return render(request, 'news/redaction.html', data)

# Удаление статьи
def delete_article(request, articles_id3): 
	try:
		obj = Articles.objects.get(id = articles_id3)
		if request.user.id == obj.id_user: ##3 Типо защита, хЕх
			obj.delete()
			return redirect('news:news_home')
		else:
			raise Http404("Иди гуляй, мамин хакер")	
	except:
		raise Http404("Статья не найдена")			
		
		
#Создание статьи		
def create(request):
	a = ''
	if request.method == 'POST':
		a = request.POST["file"]
		create_article = Articles(id_user = request.user.id, 
								  title = request.POST["title"],
								  anons = request.POST["anons"],
								  full_text = request.POST["full_text"],
								  my_photo = request.POST["file"],
								  date = timezone.datetime.now() 						
								)	
		create_article.save()	

	data = {
		"a": a
 	}	
	

	return render(request, 'news/create.html', data)	

	

		
