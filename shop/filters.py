from django_filters import rest_framework

from shop.models import Product


class ProductFilters(rest_framework.FilterSet):
    category = rest_framework.CharFilter(
        field_name='category',
        lookup_expr='name__icontains',
        label="Category",
    )
    description = rest_framework.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        label='Description'
    )
    price_min = rest_framework.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Minimum Price'
    )
    price_max = rest_framework.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Maximum Price'
    )
    tags = rest_framework.CharFilter(field_name='tags', lookup_expr='name')

    class Meta:
        model = Product
        fields = ('name', 'rating')
