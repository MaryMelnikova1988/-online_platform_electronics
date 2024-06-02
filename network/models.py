from django.db import models


class NetworkObject(models.Model):
    TYPE = [
        ('Factory', 'Завод'),
        ('Retail network', 'Розничная сеть'),
        ('Individual entrepreneur', 'Индивидуальный предприниматель')
    ]

    LEVEL = [
        ('0', 'уровень 0'),
        ('1', 'уровень 1'),
        ('2', 'уровень 2')
    ]

    type = models.CharField(max_length=60, choices=TYPE, verbose_name='Тип звена сети')
    level = models.CharField(max_length=10, choices=LEVEL, verbose_name='Уровень в иерархии поставок')

    name = models.CharField(max_length=250, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', null=True, blank=True)
    debt_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        verbose_name='Задолженность перед поставщиком', null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.type}:{self.name}'

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)
    networkObject = models.ForeignKey('NetworkObject', on_delete=models.CASCADE, verbose_name='Объект сети')

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
