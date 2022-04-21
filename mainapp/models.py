from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    """Модель товаров"""
    title = models.CharField(max_length=64, verbose_name='наименование')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name='стоимость')

    def __str__(self):
        return f'{self.title}({self.price})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']
