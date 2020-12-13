from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_init, pre_save
from django.dispatch import receiver


class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    # orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order')
    quantity = models.PositiveIntegerField(default=0)


# @receiver(signal=post_save, sender=Order)
# def manage(sender, instance, created, **kwargs):
#     if instance.item.quantity >= instance.quantity:
#         instance.item.quantity = instance.item.quantity - instance.quantity
#         instance.item.orders = instance.item.orders + 1
#         instance.item.save()
#
#     else:
#         return {'error': 'quantity is smaller'}

