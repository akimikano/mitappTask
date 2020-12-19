from django.db import transaction
from django.db.models import Count, IntegerField
from rest_framework import status, request
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Item, Order, MainOrder
from .serializers import ItemSerializer, OrderSerializer, MainOrderSerializer, ItemListSerializer




class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        obj = Item.objects.prefetch_related('order').annotate(order_count=Count('order')).get(pk=kwargs['pk'])
        serializer = ItemSerializer(obj)
        return Response(serializer.data)


class OrderView(ModelViewSet):
    queryset = Order.objects.select_related('item')
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        quantity = serializer.validated_data['quantity']
        item = serializer.validated_data['item']
        if quantity <= item.quantity:
            item.quantity = item.quantity - quantity
            item.save()
            serializer.save()
        else:
            raise ValidationError('Недостаточно в наличии')


class MainOrderView(ModelViewSet):
    queryset = MainOrder.objects.prefetch_related('orders')
    serializer_class = MainOrderSerializer







