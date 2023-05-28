from django.db import models
from main.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    address = models.CharField(max_length=250,verbose_name='Адрес')
    phoneNumber = models.CharField(max_length=12,verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    paid = models.BooleanField(default=False,verbose_name='Выполнен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.DO_NOTHING,verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity