from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from taggit.models import Tag
from taggit.serializers import TaggitSerializer, TagListSerializerField

from shop.filters import ProductFilters, ReviewsFilterSet
from shop.models import Category, Product, Review
from shop.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, TagSerializer


# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
    search_fields = ["name"]
    filterset_fields = ['name']


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    queryset = Product.objects.all()
    filterset_class = ProductFilters


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['review__icontains']
    filterset_class = ReviewsFilterSet

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






