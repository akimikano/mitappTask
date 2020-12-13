from django.urls import path
from .views import ItemView, OrderView

urlpatterns = [
    path('items/', ItemView.as_view({'get': 'list', 'post': 'create'})),
    path('items/<int:pk>/', ItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('orders/', OrderView.as_view({'post': 'create', 'get': 'list'})),
    path('orders/<int:pk>/', OrderView.as_view({'get': 'retrieve', 'delete': 'destroy'})),

]
