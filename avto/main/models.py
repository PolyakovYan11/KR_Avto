from django.db import models

body_list = (
    [1, 'Выберите кузов...'],
    [2, 'Седан'],
    [3, 'Хэтчбек 3 дв.'],
    [4, 'Хэтчбек 5 дв.'],
    [5, 'Лифтбек'],
    [6, 'Внедорожник'],
    [7, 'Универсал'],
    [8, 'Купе'],
    [9, 'Минивэн'],
    [10, 'Лимузин'],
    [11, 'Кабриолет'],
)

shift_list = (
    [1, 'Выберите кпп...'],
    [2, 'Автоматическая'],
    [3, 'Робот'],
    [4, 'Механическая']
)

engine_list = (
    [1, 'Выберите тип двигателя...'],
    [2, 'Бензин'],
    [3, 'Дизель'],
    [4, 'Гибрид'],
    [5, 'Электро']
)

volume_list = (
    [1, 'Выберите объем двигателя...'],
    [2, '0.2 л'],
    [3, '0.3 л'],
    [4, '0.4 л'],
    [5, '0.5 л'],
    [6, '0.6 л'],
    [7, '0.7 л'],
    [8, '0.8 л'],
    [9, '0.9 л'],
    [10, '1.0 л'],
    [11, '1.1 л'],
    [12, '1.2 л'],
    [13, '1.3 л'],
    [14, '1.4 л'],
    [15, '1.5 л'],
    [16, '1.6 л'],
    [17, '1.7 л'],
    [18, '1.8 л'],
    [19, '1.9 л'],
    [20, '2.0 л'],
    [21, '2.1 л'],
    [22, '2.2 л'],
    [23, '2.3 л'],
    [24, '2.4 л'],
    [25, '2.5 л'],
    [26, '2.6 л'],
    [27, '2.7 л'],
    [28, '2.8 л'],
    [29, '2.9 л'],
    [30, '3.0 л'],
    [31, '3.5 л'],
    [32, '4.0 л'],
    [33, '4.5 л'],
    [34, '5.0 л'],
    [35, '5.5 л'],
    [36, '6.0 л'],
    [37, '7.0 л'],
    [38, '8.0 л'],
    [39, '9.0 л'],
    [40, '10.0 л']

)

driveunit_list = (
    [1, 'Выберите привод...'],
    [2, 'Передний'],
    [3, 'Задний'],
    [4, 'Полный']
)


class Ad(models.Model):
    mark = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    age = models.IntegerField('Год')
    body = models.IntegerField('Кузов', choices=body_list, default=1)
    shift = models.IntegerField('КПП', choices=shift_list, default=1)
    mileage = models.IntegerField('Пробег')
    engine = models.IntegerField('Двигатель', choices=engine_list, default=1)
    volume = models.IntegerField('Объем двигателя', choices=volume_list, default=1)
    driveunit = models.IntegerField('Привод', choices=driveunit_list, default=1)
    vin = models.CharField('VIN', max_length=17)
    city = models.CharField('Город', max_length=50)
    price = models.IntegerField('Цена')
    comment = models.CharField('Комментарий', max_length=1000)

    def __str__(self):
        return self.mark
