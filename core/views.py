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
        })
