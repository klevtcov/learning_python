from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.urls import reverse


# Create your models here.

'''
Id - INT
Title - Varchar
Content - Text
created_at - DateTime
updated_at - DateTime
photo - image
is_published - Boolean
'''

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование') # Передаем название полей отдельным аргументом
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name='Фото', blank=True) # Blank - поле не обязательно к заполнению 
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория') # Создаём поле и привязываем его к модели категорий. null=True - для обязательного поля, добавленного позже позволяет заполнить по имеющимся строкам пустые значения. default - пропишет значение по умолчанию
    views = models.IntegerField(default=0) # Счетчик просмотров, по умолчанию 0

    def my_func(self):
        return 'Hello from model'

# возвращаем не объект <News: News object (1)>, а его название
# News.objects.all()
# str - сторокое представление объекта
    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        # return reverse('view_news', kwargs={'news_id': self.pk})
        return reverse('view_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость' # Имя в единственном числе
        verbose_name_plural = 'Новости' # Имя во множественном числе
        ordering = ['-created_at'] # Порядок сортировки полей. Можно теперь не указывать порядок сортировки при выводе в views.py

# Добавляем класс (таблицу) с категориями
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории') #db_index - индексирует поле для более быстрого доступа

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title  

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


