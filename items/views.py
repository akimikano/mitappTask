from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer


class ItemView(ModelViewSet):
    queryset = Item.objects.prefetch_related('order').annotate(order_count=Count('order'))
    serializer_class = ItemSerializer
    lookup_field = 'pk'


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'






