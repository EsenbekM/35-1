'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
принимает следующие аргументы:
request - запрос от пользователя (объект HttpRequest) параметр обязательный
template_name - имя шаблона (строка) параметр обязательный
context - словарь с данными (dict) параметр необязательный
content_type - тип контента (строка) параметр необязательный например 'text/html', 'application/json' и т.д. по умолчанию 'text/html'
status - статус ответа (число) параметр необязательный например 200, 404, 500 и т.д. по умолчанию 200 (OK)
using - имя базы данных (строка) параметр необязательный по умолчанию None (основная база данных) Нужен для работы с несколькими базами данных (подробнее в документации https://docs.djangoproject.com/en/3.2/topics/db/multi-db/) 

QuerySet - набор объектов, полученных в результате запроса к базе данных.


ORM - Object-Relational Mapping - объектно-реляционное отображение. 
Это технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования, 
создавая «виртуальную объектную базу данных». В Django ORM реализован с помощью классов моделей.

objects - менеджер модели. Менеджер модели - это интерфейс для взаимодействия с базой данных.
Менеджер позволяет обращаться к базе данных с помощью следующих методов:
.all(), .filter(), .exclude(), .get(), .create(), .update(), .delete() и т.д. 
(подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

Field lookups - поиск по полям. Поиск по полям позволяет получить объекты, у которых значение поля удовлетворяет условию.
__icontains - нечувствительный к регистру поиск подстроки в строке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#icontains)
__contains - чувствительный к регистру поиск подстроки в строке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#contains)\
__in - поиск в списке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#in)
__gt - больше (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#gt)
__gte - больше или равно (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#gte)
__lt - меньше (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#lt)
__lte - меньше или равно (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#lte)
__range - в диапазоне (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#range)
__year - год (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#year)
__month - месяц (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#month)
__day - день (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#day)
__week_day - день недели (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#week-day)
__hour - час (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#hour)
__minute - минута (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#minute)
__second - секунда (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#second)
__isnull - проверка на None (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#isnull)
__exact - точное совпадение (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#exact)
__iexact - нечувствительный к регистру поиск точного совпадения (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iexact)
__startswith - начинается с (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#startswith)
__istartswith - нечувствительный к регистру поиск начинается с (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#istartswith)
__endswith - заканчивается на (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#endswith)
__iendswith - нечувствительный к регистру поиск заканчивается на (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iendswith)
__regex - регулярное выражение (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#regex)
__iregex - нечувствительный к регистру поиск регулярного выражения (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iregex)

Можно использовать с помощью методов:
.filter(), .exclude(), .get(), .create(), .update(), .delete() и т.д.
Например:
Post.objects.filter(title__icontains='привет', author__username='admin')
Можно комбинировать несколько поисковых фильтров, например:
Post.objects.filter(title__icontains='привет', author__username='admin')

Также через 2 подчеркивания можно обращаться к полям связанных моделей, например:
Post.objects.filter(author__username='admin')
Post.objects.filter(author__username__icontains='admin')
Таким образом мы можем получить все посты, у которых автор имеет имя admin.

pagination - пагинация. Пагинация - это разбиение большого количества данных на страницы.

Pagination formula: 
start = (page - 1) * limit
end = page * limit

[|0, 1, 2,| 3, 4, 5,| 6, 7, 8,| 9] - список объектов
10 / 3 = 3.3333333333333335 = 4 - количество страниц

page = 4
limit = 3
start = (4-1) * 3 = 9
end = 3 * 3 = 9

page - номер страницы
limit - количество объектов на странице
start - индекс первого объекта на странице
end - индекс последнего объекта на странице
list[start:end] - срез списка, который содержит объекты на странице

query parameters - параметры запроса. 
Параметры запроса - это часть URL, которая начинается с ? и содержит пары ключ=значение, разделенные &.
'''
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings

from post.models import Post, Comments, Hashtag
from post.forms import PostForm, PostForm2, CommentForm


def main_view(request):
    if request.method == 'GET': # GET - получение данных 
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        # 1 - получить все посты из базы данных
        posts = Post.objects.all() # QuerySet

        search = request.GET.get('search')
        order = request.GET.get('order')
        
        if search:
            # posts = posts.filter(title__icontains=search) | posts.filter(text__icontains=search)
            # | - оператор ИЛИ (OR)
            # & - оператор И (AND)
            posts = posts.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )

        if order == 'date':
            posts = posts.order_by('created_at')

        if order == '-date':
            posts = posts.order_by('-created_at')

        if order == 'rate':
            posts = posts.order_by('rate')


        max_page = posts.__len__() / settings.OBJECT_PER_PAGE

        # 105 / 10 = 10.5 = 11

        if round(max_page) < max_page:
            max_page += 1
        else:
            max_page = round(max_page)


        page = request.GET.get('page', 1)

        start = (int(page) - 1) * settings.OBJECT_PER_PAGE
        end = int(page) * settings.OBJECT_PER_PAGE

        # Formula: 
        # start = (page - 1) * limit
        # end = page * limit

        # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]

        # example 1:
        # page = 1
        # limit = 3
        # start = (1-1) * 3 = 0
        # end = 1 * 3 = 3
        # posts[start:end] = [post1, post2, post3]

        # example 2:
        # page = 2
        # limit = 3
        # start = (2-1) * 3 = 3
        # end = 2 * 3 = 6
        # posts[start:end] = [post4, post5, post6]

        # example 3:
        # page = 3
        # limit = 3
        # start = (3-1) * 3 = 6
        # end = 3 * 3 = 9
        # posts[start:end] = [post7, post8, post9]

        # example 4:
        # page = 4
        # limit = 3
        # start = (4-1) * 3 = 9
        # end = 4 * 3 = 12
        # posts[start:end] = [post10]

        # 2 - передать посты в шаблон
        context = {
            'posts': posts[start:end],
            'max_page': range(1, int(max_page) + 1),
        }

        # 3 - вернуть ответ с шаблоном и данными
        return render(
            request, # запрос от пользователя (объект HttpRequest) параметр обязательный
            'post/list.html',  # имя шаблона (строка) параметр обязательный
            context=context # словарь с данными (dict) параметр необязательный
        )
    

def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(request, '404.html')
        
        context = {
            'post': post,
            'form': CommentForm,
        }

        return render(
            request, # запрос от пользователя (объект HttpRequest) параметр обязательный
            'post/detail.html',  # имя шаблона (строка) параметр обязательный
            context=context # словарь с данными (dict) параметр необязательный
        )


def post_update_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, '404.html')
    
    if request.method == 'GET':
        context = {
            'form': PostForm2(instance=post),
            'post': post,
        }
        return render(request, 'post/update.html', context=context)

    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            context = {
                'form': form,
                'post': post,
            }
            return render(request, 'post/update.html', context=context)


def hashtag_list_view(request):
    if request.method == 'GET':
        # 1 - получить все хэштеги из базы данных
        hashtags = Hashtag.objects.all()

        # 2 - передать хэштеги в шаблон
        context = {
            'hashtags': hashtags,
        }

        # 3 - вернуть ответ с шаблоном и данными
        return render(
            request, # запрос от пользователя (объект HttpRequest) параметр обязательный
            'hashtag/list.html',  # имя шаблона (строка) параметр обязательный
            context=context # словарь с данными (dict) параметр необязательный
        )
    

def posts_create_view(requests):
    if requests.method == 'GET':
        # отобразить форму
        context = {
            'form': PostForm2,
        }
        return render(requests, 'post/create.html', context=context)

    if requests.method == 'POST': # создать пост
        # 1 - получить данные из запроса
        form = PostForm2(requests.POST, requests.FILES)

        # 2 - валидация данных
        if form.is_valid(): # True если форма валидна, False если форма не валидна
            # 3 - создать пост
            # cleaned_data - это словарь с данными, которые прошли валидацию
            
            # Если это Form, Post.objects.create(**form.cleaned_data)
            # Post.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save() # создает пост в базе данных и возвращает объект поста (Post)

            return redirect('/posts/')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'post/create.html', context=context)


def comment_create_view(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(request, '404.html')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.save()

            return redirect(f'/posts/{post_id}/')
        else:
            context = {
                'post': post,
                'form': form,
            }

            return render(request, 'post/detail.html', context=context)
