from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import reverse
from rest_framework.views import APIView


# Create your views here.


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "users_url": reverse.reverse_lazy('users:user-list', request=request),
            'categories_url': reverse.reverse_lazy('shop:category-list', request=request),
            'products_url': reverse.reverse_lazy('shop:product-list', request=request),
            'products_reviews_url': reverse.reverse_lazy('shop:review-list', request=request),
            'orders_url': reverse.reverse_lazy('order:order-list', request=request),
            'order_items_url': reverse.reverse_lazy('order:item-list', request=request),
            'payments_url': reverse.reverse_lazy('payment:payment-list', request=request),
            'transaction_url': reverse.reverse_lazy('payment:transaction-list', request=request),
            'tags': reverse.reverse_lazy('shop:tag-list', request=request),
        })
