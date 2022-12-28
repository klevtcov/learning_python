from dataclasses import field
from subprocess import call
from tkinter import Widget
from django import forms


# Импортируем модель 
from .models import News

# импортируем библиотеку для регулярок
import re

# импортируем класс ошибки валидации
from django.core.exceptions import ValidationError

# импортируем формы
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# капча
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    captha = CaptchaField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='От 3-х до 150-ти символов', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    

class NewsForm(forms.ModelForm):
    # Форма связанная с моделью
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows" : 5}), 
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title







'''
# from .models import Category - нужна для не связанной формы, для подгруски списка категорий

Форма не связанная с моделью. Наследование от класса Форм
class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows" : 5
        }))
    is_published = forms.BooleanField(label='Опубликовано?', initial=True)
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), empty_label='Выберите категорию', widget=forms.Select(attrs={"class": "form-control"}))

'''