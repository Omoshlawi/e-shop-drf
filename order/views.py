from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer


# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = [
        'get',
        'post'
    ]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
