from django.contrib import admin

from .models import News, Category

from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms


# Register your models here.

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


# Настраиваем поля приложения в админке
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title') # Какие поля будут ссылкой на новость
    search_fields = ('title', 'content') # Добавление поиска и список полей, по которым он будет производиться
    list_editable = ('is_published',) # Добавляем возможность редактировать поля прямо из таблицы
    list_filter = ('is_published', 'category') # Добавляем фильтры к полям
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">')
        else:
            return '–'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title') # Какие поля будут ссылкой на новость
    search_fields = ('title',) # Добавление поиска и список полей, по которым он будет производиться. Тк кортеж, мы должны явно указать перечисление, добавив запятую


admin.site.register(News, NewsAdmin) # Подключаем приложение в админку и настройки отображения
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
