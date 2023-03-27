from django.shortcuts import render
from rest_framework import viewsets

from shop.filters import ProductFilters
from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer


# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
    search_fields = ["name"]
    filterset_fields = ['name']


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    queryset = Product.objects.all()
    filterset_class = ProductFilters



