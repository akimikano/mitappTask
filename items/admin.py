from django.contrib import admin
from items.models import Item, Order

admin.site.register(Item)
admin.site.register(Order)