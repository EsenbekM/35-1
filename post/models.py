'''
models.py - Файл моделей приложения. 

migration - Файлы миграций.

'''

from django.db import models


class Post(models.Model):
    image = models.ImageField(
        upload_to='posts', null=True, blank=False,
        verbose_name="Фото"
        )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    rate = models.FloatField(default=0, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
