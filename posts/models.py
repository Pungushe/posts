from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    artist = models.CharField(max_length=500, null=True, verbose_name='Художник')
    url=models.URLField(max_length=500, null=True)
    image=models.URLField(max_length=500, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name='Автор')
    body = models.TextField(verbose_name='Текст')
    likes = models.ManyToManyField(User, related_name='likedposts', through='LikedPost')
    tags = models.ManyToManyField('Tag', verbose_name='Tеги')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id=models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return str(self.title)

class LikedPost(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    class Meta:
        ordering=['-created']
        verbose_name='Лайк поста'
        verbose_name_plural='Лайки постов'
    def __str__(self):
        return f'{self.user.username} : {self.post.title}'

class Tag(models.Model):
    name=models.CharField(max_length=20, verbose_name='Название')
    image = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Изображение')
    slug=models.SlugField(max_length=20, unique=True)
    order=models.IntegerField(null=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Тег'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    body = models.CharField(max_length=150, verbose_name='Текст')
    likes = models.ManyToManyField(User, related_name='likedcomments', through='LikedComment')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id=models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering=['-created']
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'неизвестный автор : {self.body[:30]}'

class LikedComment(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Пост')
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    class Meta:
        ordering=['-created']
        verbose_name='Лайк комментария'
        verbose_name_plural='Лайки комментариев'
    def __str__(self):
        return f'{self.user.username} : {self.comment.body[:30]}'

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies', verbose_name='Автор')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies', verbose_name='Комментарий')
    body = models.CharField(max_length=150, verbose_name='Текст')
    likes = models.ManyToManyField(User, related_name='likedreplies', through='LikedReply')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id=models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering=['-created']
        verbose_name='Ответ'
        verbose_name_plural='Ответы'

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'неизвестный автор : {self.body[:30]}'

class LikedReply(models.Model):
    reply=models.ForeignKey(Reply, on_delete=models.CASCADE, verbose_name='Пост')
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    class Meta:
        ordering=['-created']
        verbose_name='Лайк отвата'
        verbose_name_plural='Лайки ответов'
    def __str__(self):
        return f'{self.user.username} : {self.reply.body[:30]}'
