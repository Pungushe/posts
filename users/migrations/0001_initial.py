# Generated by Django 4.2.6 on 2023-10-27 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар')),
                ('real_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email')),
                ('location', models.CharField(blank=True, max_length=20, null=True, verbose_name='Место проживание')),
                ('bio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место работы')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
