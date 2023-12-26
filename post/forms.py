from django import forms

from post.models import Post


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
        