# Generated by Django 4.2.6 on 2023-10-30 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('body', models.CharField(max_length=150, verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LikedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Лайк поста',
                'verbose_name_plural': 'Лайки постов',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LikedReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Лайк отвата',
                'verbose_name_plural': 'Лайки ответов',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('image', models.FileField(blank=True, null=True, upload_to='icons/', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Тэги',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('body', models.CharField(max_length=150, verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.comment', verbose_name='Комментарий')),
                ('likes', models.ManyToManyField(related_name='likedreplies', through='posts.LikedReply', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('artist', models.CharField(max_length=500, null=True, verbose_name='Художник')),
                ('url', models.URLField(max_length=500, null=True)),
                ('image', models.URLField(max_length=500, verbose_name='Изображение')),
                ('body', models.TextField(verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('likes', models.ManyToManyField(related_name='likedposts', through='posts.LikedPost', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='posts.tag', verbose_name='Tеги')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='likedreply',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.reply', verbose_name='Пост'),
        ),
        migrations.AddField(
            model_name='likedreply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='likedpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Пост'),
        ),
        migrations.AddField(
            model_name='likedpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='LikedComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Лайк комментария',
                'verbose_name_plural': 'Лайки комментариев',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='likedcomments', through='posts.LikedComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name='Пост'),
        ),
    ]
