from django.db import models


class Record(models.Model):
    head = models.CharField(max_length=30, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/', verbose_name='Превью')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_number = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.head}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['head']
