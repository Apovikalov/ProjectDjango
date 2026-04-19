from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.CharField(max_length=30, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания')
    last_changed_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
