from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_init, pre_save
from django.dispatch import receiver


class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    # orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class MainOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order', null=True)
    quantity = models.PositiveIntegerField(null=True, verbose_name='quantity')
    main_order = models.ForeignKey(MainOrder, on_delete=models.CASCADE, related_name='orders', null=True)













