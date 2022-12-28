from email import message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import News, Category
from .forms import ContactForm, NewsForm, UserRegisterForm, UserLoginForm, ContactForm

# контроллеры класса
from django.views.generic import ListView, DetailView, CreateView

from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# импортируем методы для авторицазии
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator

from django.contrib import messages

from django.core.mail import send_mail

#  можно редиректить на кастомную страницу
# from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'djangolearning@mail.ru', ['klevtsov.s@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправленно')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'news/contact.html', {'form': form})
    # objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8']
    # paginator = Paginator(objects, 2)
    # page_num = request.GET.get('page', 1)
    # page_objects = paginator.get_page(page_num)
    # return render(request, 'news/test.html', {'page_obj': page_objects})


# пишем контроллеры класса, которые заменять функции index categories
class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 5
    # mixin_prop = 'hello world'
    # для статики можно использовать extra_context
    # extra_context = {'title': 'Главная'}

    # взяли данные из контекста, дополнили требуемыми
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        # context['title'] = 'Главная страница'
        # context['mixin_prop'] = self.get_prop()
        return context

    # Фильтруем данные, которые будут отдаваться по запросу
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')

class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    #  и поменять маршрут
    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published=True).select_related('category')

class ViewNews(MyMixin, DetailView):
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'
    model = News
    context_object_name = 'news_item'

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    # по умолчанию редирект на сам объект, т.к. есть метод get_absolute_url в модели
    # success_url = reverse_lazy('home')
    template_name = 'news/add_news.html'
    login_url = '/admin/'
    # redirect_field_name = 'redirect_to'
    # raise_exception = True



'''
def index(request):
    # print(dir(request))

    # res = '<h1>Список новостей</h1>'    
    # for item in news:
    #     res += f'<div>\n <p> {item.title} </p>\n <p> {item.content} </p>\n </div> \n <hr>\n'
    # return HttpResponse(res)

    # return render(request, 'news/index.html', {'news': news, 'title' : 'Список новостей'}

    # news = News.objects.all() Выводим в обратном порядке, от самых новых к старым
    # При наличии сортировки внутри Meta модели (models.py), порядок сортировки тут можно не указывать
    # news = News.objects.order_by('-created_at')

    news = News.objects.all()
    # categories = Category.objects.all()
    context = {
        'news': news, 
        'title' : 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)
'''

'''
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})
'''

'''
def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})
'''

'''
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # распаковка словаря по-питонячьи. распакует словарь и присвоит ключам значения
            # news = News.objects.create(**form.cleaned_data) - для не связанных форм приходится пользоваться методами объекта
            # для связанных форм есть свой метод:
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
'''