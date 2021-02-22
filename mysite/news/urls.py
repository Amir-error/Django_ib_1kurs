from . import views    # news
from django.urls import path

app_name = 'news'  # ВАЖНО ДЛЯ ПРАВИЛЬНОГО ОБРАЩЕНИЯ ПО ПСЕВДОНИМУ
urlpatterns = [
	path('', views.news_home, name = "news_home"),  # Смотрит куда дальше нам нужно, параметр name именнованая ссылка / псевдрним
	path('create/', views.create, name = "create"),
	path('<int:articles_id>/', views.detailview, name = 'detailview'), # Отслеживаем динам параметр. 
	path('<int:articles_id>/<int:articles_id2>/', views.redaction, name = 'redaction'),
	path('delete/<int:articles_id3>/', views.delete_article, name = 'delete_article'),
]