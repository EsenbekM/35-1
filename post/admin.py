'''
admin.py - Файл настроек административного сайта.

admin - модуль для работы с административным сайтом.
site - объект, который представляет собой административный сайт.
register - метод, который регистрирует модель в административном сайте. (простая регистрация)

@admin.register(SomeModel) - декоратор, который регистрирует модель в административном сайте. (расширенная регистрация)  
наследование от admin.ModelAdmin - класс, который содержит настройки для модели в административном сайте.
'''

from django.contrib import admin
from django.http.request import HttpRequest # модуль для работы с административным сайтом.

from post.models import Post, Comments, Hashtag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'created_at', 'updated_at'] # Поля, которые будут отображаться в административном сайте
    list_display_links = ['id', 'title'] # Поля, которые будут ссылками
    # readonly_fields = ['title', 'rate'] # Поля, которые будут только для чтения
    search_fields = ['title', 'text'] # Поля, по которым будет осуществляться поиск
    list_filter = ['rate', 'created_at'] # Поля, по которым будет осуществляться фильтрация
    ordering = ['created_at'] # Поля, по которым будет осуществляться сортировка

    # def has_add_permission(self, request: HttpRequest) -> bool: 
    #'''Метод, который проверяет, есть ли у пользователя права на добавление записи в административном сайте'''
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    # '''Метод, который проверяет, есть ли у пользователя права на удаление записи в административном сайте'''
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    # '''Метод, который проверяет, есть ли у пользователя права на изменение записи в административном сайте'''
    #     return False

admin.site.register(Comments)

admin.site.register(Hashtag)
