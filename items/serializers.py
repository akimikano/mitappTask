from django.db import transaction, DatabaseError
from rest_framework import serializers
from items.models import Item, Order, MainOrder
from rest_framework.exceptions import ValidationError


class OrderSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', allow_null=True, read_only=True)
    total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'item', 'quantity', 'item_name', 'total_price']


class ItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True, read_only=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'quantity', 'price', 'order', 'order_count')


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'quantity', 'price')


class MainOrderSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(allow_null=False, many=True)

    class Meta:
        model = MainOrder
        fields = ('id', 'orders',)

    @transaction.atomic
    def create(self, validated_data):
        print(validated_data)
        orders = validated_data.pop('orders')
        main_order = MainOrder.objects.create(**validated_data)
        orderObjects = []

        for order in orders:
            if order['quantity'] <= order['item'].quantity:
                # Order.objects.create(**order, main_order=main_order)
                order['item'].quantity = order['item'].quantity - order['quantity']
                order['item'].save()
                orderObjects.append(Order(**order, main_order=main_order))
            else:
                raise ValidationError('Недостаточно в наличии')
        Order.objects.bulk_create(orderObjects)
        return main_order







