from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    """Модель товаров"""
    title = models.CharField(max_length=64, verbose_name='наименование')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name='стоимость')
    # поле quantity необходимо перенести в другую модель
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title}({self.price})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']

    @property
    def item_cost(self):
        return self.quantity * self.price


# class CashRegisterCheck(models.Model):
#     """Чек"""
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class CashRegisterCheckItem(models.Model):
#     """Товары из чека"""
#     order = models.ForeignKey(CashRegisterCheck, on_delete=models.CASCADE, related_name='чек')
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cash_register_check_item')
#     quantity = models.PositiveSmallIntegerField(default=0)
