# Generated by Django 4.2 on 2024-06-02 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Factory', 'Завод'), ('Retail network', 'Розничная сеть'), ('Individual entrepreneur', 'Индивидуальный предприниматель')], max_length=60, verbose_name='Тип звена сети')),
                ('level', models.CharField(choices=[('0', 'уровень 0'), ('1', 'уровень 1'), ('2', 'уровень 2')], max_length=10, verbose_name='Уровень в иерархии поставок')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt_supplier', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Задолженность перед поставщиком')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network.networkobject', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Объект сети',
                'verbose_name_plural': 'Объекты сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')),
                ('networkObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.networkobject', verbose_name='Объект сети')),
            ],
        ),
    ]
