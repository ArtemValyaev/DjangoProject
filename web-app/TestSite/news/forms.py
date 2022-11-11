
from django.db import models
from .models import Articles, Comment
from django.forms import ModelForm, TextInput, Textarea, FileInput


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'img', 'anons', 'full_text', 'categories']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            'img': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Поделитесь мыслями',
            }),}

class DeleteCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['status']
        widgets = {
            'status': TextInput(attrs={
                'style': 'display: none',
                'placeholder': '',
            }),}