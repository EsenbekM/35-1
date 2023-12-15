'''
models.py - Файл моделей приложения. 

migration - Файлы миграций.

'''

from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=False)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"
