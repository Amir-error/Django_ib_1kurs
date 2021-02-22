from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Registration(models.Model):
	name = models.CharField('Имя', max_length = 20)
	surname = models.CharField('Фамилия', max_length = 20)
	password = models.CharField('Пароль', max_length = 15, default = 'admin')  # Нужно было умолчание, из-за отстутвия паролей у предыдущих пользователей
	age = models.IntegerField('Возраст')
	date = models.DateTimeField('Дата регистрации')

	def __str__(self):
		return self.name

	def difference_time(self):      #3  Разница времени True / False
		return self.date >= (timezone.now() - datetime.timedelta(days = 7))

	def time_now():	   ## Дата сейчас
		return timezone.datetime.now()

	class Meta:
		verbose_name = 'Регистрация'
		verbose_name_plural = 'Регистрации'

class Registration2(models.Model):
	name = models.CharField('Имя', max_length = 20)
	surname = models.CharField('Фамилия', max_length = 20)
	password = models.CharField('Пароль', max_length = 15, default = 'admin')  # Нужно было умолчание, из-за отстутвия паролей у предыдущих пользователей
	age = models.IntegerField('Возраст')
	date = models.DateTimeField('Дата регистрации')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Регистрация2'
		verbose_name_plural = 'Регистрации2'