from django.contrib import admin
from .models import Articles #импорттируем из нашего репозитория нашу модель
# Register your models here. Регистрируем нашу модель
admin.site.register(Articles) #Регистрируем БДшку
