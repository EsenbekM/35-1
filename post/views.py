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


def test_view(request):
    if request.method == 'GET': # GET - получение данных 
        posts = Post.objects.all() # SELECT * FROM post_post; return QuerySet
        print(posts)
        for post in posts:
            print(post.title)
            print(post.text)
            print(post.rate)
            print(post.created_at)
            print(post.updated_at)
            print(post.image)
            print(post.id)
            
        return HttpResponse('Test views')
    

def hello_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
