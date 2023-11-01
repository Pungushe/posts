from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image=models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    real_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Имя')
    email=models.EmailField(unique=True, null=True, verbose_name='Email')
    location = models.CharField(max_length=20, null=True, blank=True, verbose_name='Место проживание')
    bio=models.CharField(max_length=100, null=True, blank=True, verbose_name='Место работы')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)

    @property
    def avatar(self):
        try:
            avatar= self.image.url
        except:
            avatar= static('images/avatar_default.svg')
        return avatar

    @property
    def name(self):
        if self.real_name:
            name= self.real_name
        else:
            name= self.user.username
        return name