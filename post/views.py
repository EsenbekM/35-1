'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
'''
from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    if request.method == 'GET': # GET - получение данных 
        return HttpResponse('Test views')
    

def hello_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
