from rest_framework import serializers
from items.models import Item, Order


class OrderSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'item', 'quantity']


class ItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'quantity', 'order', 'order_count')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id']