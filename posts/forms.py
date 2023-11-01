from django import forms
from django.forms import ModelForm

from . models import Comment, Post, Reply


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Подпись',
            'tags': 'Категории',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder':'Добавьте подпись...', 'class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder':'Добавьте url...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Категории',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Добавьте комментарий...'}),
        }
        labels = {
            'body': '',
        }
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Добавьте ответ...', 'class': 'text-sm'}),
        }
        labels = {
            'body': '',
        }