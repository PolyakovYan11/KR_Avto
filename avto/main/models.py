from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import json

from .managers import CustomUserManager

body_list = (
    ['Седан', 'Седан'],
    ['Хэтчбек 3 дв.', 'Хэтчбек 3 дв.'],
    ['Хэтчбек 5 дв.', 'Хэтчбек 5 дв.'],
    ['Лифтбек', 'Лифтбек'],
    ['Внедорожник', 'Внедорожник'],
    ['Универсал', 'Универсал'],
    ['Купе', 'Купе'],
    ['Минивэн', 'Минивэн'],
    ['Лимузин', 'Лимузин'],
    ['Кабриолет', 'Кабриолет'],
)

shift_list = (
    ['Автоматическая', 'Автоматическая'],
    ['Робот', 'Робот'],
    ['Механическая', 'Механическая']
)

engine_list = (
    ['Бензин', 'Бензин'],
    ['Дизель', 'Дизель'],
    ['Гибрид', 'Гибрид'],
    ['Электро', 'Электро']
)

volume_list = (
    ['0.2 л', '0.2 л'],
    ['0.3 л', '0.3 л'],
    ['0.4 л', '0.4 л'],
    ['0.5 л', '0.5 л'],
    ['0.6 л', '0.6 л'],
    ['0.7 л', '0.7 л'],
    ['0.8 л', '0.8 л'],
    ['0.9 л', '0.9 л'],
    ['1.0 л', '1.0 л'],
    ['1.1 л', '1.1 л'],
    ['1.2 л', '1.2 л'],
    ['1.3 л', '1.3 л'],
    ['1.4 л', '1.4 л'],
    ['1.5 л', '1.5 л'],
    ['1.6 л', '1.6 л'],
    ['1.7 л', '1.7 л'],
    ['1.8 л', '1.8 л'],
    ['1.9 л', '1.9 л'],
    ['2.0 л', '2.0 л'],
    ['2.1 л', '2.1 л'],
    ['2.2 л', '2.2 л'],
    ['2.3 л', '2.3 л'],
    ['2.4 л', '2.4 л'],
    ['2.5 л', '2.5 л'],
    ['2.6 л', '2.6 л'],
    ['2.7 л', '2.7 л'],
    ['2.8 л', '2.8 л'],
    ['2.9 л', '2.9 л'],
    ['3.0 л', '3.0 л'],
    ['3.5 л', '3.5 л'],
    ['4.0 л', '4.0 л'],
    ['4.5 л', '4.5 л'],
    ['5.0 л', '5.0 л'],
    ['5.5 л', '5.5 л'],
    ['6.0 л', '6.0 л'],
    ['7.0 л', '7.0 л'],
    ['8.0 л', '8.0 л'],
    ['9.0 л', '9.0 л'],
    ['10.0 л', '10.0 л']

)

driveunit_list = (
    ['Передний', 'Передний'],
    ['Задний', 'Задний'],
    ['Полный', 'Полный']
)


class Ad(models.Model):
    mark = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    age = models.IntegerField('Год')
    body = models.CharField('Кузов', choices=body_list, max_length=50)
    shift = models.CharField('КПП', choices=shift_list, max_length=50)
    mileage = models.IntegerField('Пробег')
    engine = models.CharField('Двигатель', choices=engine_list, max_length=50)
    volume = models.CharField('Объем двигателя', choices=volume_list, max_length=50)
    driveunit = models.CharField('Привод', choices=driveunit_list, max_length=50)
    vin = models.CharField('VIN', max_length=17)
    city = models.CharField('Город', max_length=50)
    price = models.IntegerField('Цена')
    comment = models.CharField('Комментарий', max_length=1000, null=True)
    image = models.ImageField('Фото', upload_to='main/img/imgavto', default='main/img/a.jpg')
    profile = models.ForeignKey('Profiles', on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")

    def __str__(self):
        return self.mark

    def get_absolute_url(self):
        return f'/{self.id}'


class Profiles(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    uname = models.CharField('ФИО', max_length=50)
    phone_number = models.CharField('Номер телефона', null=True, max_length=16)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Favorites(models.Model):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, verbose_name="Объявление")
    profile = models.ForeignKey('Profiles', on_delete=models.CASCADE, verbose_name="Пользователь")

