from django.db import models

# Create your models here.
# Работаем внутри приложения news
class Articles(models.Model): # Создаем нашу модель , наследум класс
	id_user = models.IntegerField("Пользователь", default = 1) #Поля БДшки
	my_photo = models.ImageField(verbose_name = "Изображение")
	title = models.CharField('Название', max_length = 50)    # Поле модели, СharField определяет тип ввода  
	anons = models.CharField('Анонс', max_length = 250) 
	full_text = models.TextField('Статья')
	date = models.DateTimeField('Дата публикации')   

	def __str__(self):
		return self.title

	class Meta:   
		verbose_name = 'Новость'    # Для отображения имени 
		verbose_name_plural = 'Новости'	                 
