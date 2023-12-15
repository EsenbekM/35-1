'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.

QuerySet - набор объектов, полученных в результате запроса к базе данных.
'''
from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post


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

        return render(request, 'post/list.html', context=context)
    