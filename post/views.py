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

'''
from django.shortcuts import redirect, render
from django.http import HttpResponse
from post.models import Post, Comments, Hashtag
from post.forms import PostForm, PostForm2


def main_view(request):
    if request.method == 'GET': # GET - получение данных 
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        # 1 - получить все посты из базы данных
        posts = Post.objects.all() # QuerySet

        # 2 - передать посты в шаблон
        context = {
            'posts': posts,
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
        }

        return render(
            request, # запрос от пользователя (объект HttpRequest) параметр обязательный
            'post/detail.html',  # имя шаблона (строка) параметр обязательный
            context=context # словарь с данными (dict) параметр необязательный
        )


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
            form.save()

            return redirect('/posts/')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'post/create.html', context=context)
