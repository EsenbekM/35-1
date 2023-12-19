'''
admin.py - Файл настроек административного сайта.

admin - модуль для работы с административным сайтом.
site - объект, который представляет собой административный сайт.
register - метод, который регистрирует модель в административном сайте. (простая регистрация)
'''

from django.contrib import admin
from django.http.request import HttpRequest # модуль для работы с административным сайтом.

from post.models import Post, Comments, Hashtag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    # readonly_fields = ['title', 'rate']
    search_fields = ['title', 'text']
    list_filter = ['rate', 'created_at']
    ordering = ['created_at']

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

admin.site.register(Comments)

admin.site.register(Hashtag)
