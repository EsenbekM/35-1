"""
urls.py - Файл маршрутизации Django-проекта.

admin.site.urls - URL-адреса административного сайта.

path - функция для создания маршрута.
Принимает 2 аргумента:
1) Путь (строка)
2) Обработчик (функция, которая будет обрабатывать запрос)
"""
from django.contrib import admin
from django.urls import path
from post.views import test_view, hello_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view, name='test'),
    path('hello/', hello_view),
]