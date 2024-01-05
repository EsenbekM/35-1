'''
Форма это поля, которые мы можем заполнить и отправить на сервер.
В Django есть два класса для создания форм:

Form - класс, который описывает форму
ModelForm - класс, который описывает форму на основе модели

В класс Meta ModelForm можно добавить:
    - model - модель, на основе которой создается форма
    - fields - поля, которые будут в форме
    - exclude - поля, которые не будут в форме
    - labels - заголовки полей
    - help_texts - тексты подсказок
    - widgets - виджеты для полей

save() - метод, который сохраняет данные из формы в базу данных и возвращает объект, который был создан
save метод можно использовать только для ModelForm (не для Form), 
потому что Form не знает, как сохранять данные в базу данных (в какую таблицу и какие поля)
save метод можно также переопределить, чтобы добавить дополнительную логику при сохранении данных в базу данных
Например (см. 89стр.):
    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.author
        post.save()
        return post

commit - параметр, который указывает, нужно ли сохранять данные в базу данных
Если commit=False, то данные не будут сохранены в базу данных, но объект будет создан и возвращен
Если commit=True, то данные будут сохранены в базу данных и объект будет создан и возвращен
По умолчанию commit=True

False ставится в том случае, если нужно добавить дополнительную логику при сохранении данных в базу данных
'''
from typing import Any
from django import forms

from post.models import Post, Comments


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        min_length=3,
        label='Название поста',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Текст поста',
        required=False,
    )
    image = forms.ImageField(
        required=False,
        label='Картинка',
    )
    rate = forms.IntegerField(
        label='Рейтинг',
        required=False,
    )

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'python' not in title.lower():
            raise forms.ValidationError('В заголовке должно быть слово "python"')

        return title
    
    # def clean(self):
    #     cleaned_data = super().clean()

    #     title = cleaned_data.get('title')
    #     text = cleaned_data.get('text')

    #     if title and text and title == text:
    #         raise forms.ValidationError('Заголовок и текст не должны совпадать')
        
    #     return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'rate')
        labels = {
            'title': 'Название поста',
            'text': 'Текст поста',
            'image': 'Картинка',
            'rate': 'Рейтинг',
        }
        help_texts = {
            'title': 'Введите название поста',
            'text': 'Введите текст поста',
            'image': 'Загрузите картинку',
            'rate': 'Введите рейтинг',
        }

    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     post.author = self.author
    #     post.save()
    #     return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text', 'post')
        labels = {
            'text': 'Текст комментария',
        }
        help_texts = {
            'text': 'Введите текст комментария',
        }

    def clean(self):
        cleaned_data = super().clean()

        text = cleaned_data.get('text')

        if text and len(text) > 200:
            raise forms.ValidationError('Длина комментария не должна превышать 200 символов')

        if not text:
            raise forms.ValidationError('Комментарий не должен быть пустым')
        
        if len(text) < 3:
            raise forms.ValidationError('Длина комментария должна быть больше 3 символов')
        
        return cleaned_data
