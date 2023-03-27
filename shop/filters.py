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
    tags = rest_framework.CharFilter(
        field_name='tags',
        label="Comma separated Tags",
        method='filter_tags'
    )

    class Meta:
        model = Product
        fields = ('name', 'rating')

    def filter_tags(self, queryset, name, value):
        tags = value.replace(' ', '').split(",")
        return queryset.filter(**{'tags__name__in': tags})
