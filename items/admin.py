from django.contrib import admin
from items.models import Item, Order, MainOrder

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(MainOrder)