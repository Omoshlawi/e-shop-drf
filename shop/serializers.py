from django.db.models import Avg
from rest_framework import serializers
from taggit.models import Tag
from taggit.serializers import TaggitSerializer, TagListSerializerField

from shop.models import Category, Product, ProductImage, Review


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        "shop:category-detail", lookup_field='slug'
    )
    products = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='shop:product-detail',
        read_only=True,
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = ("url", "name", "updated", "image", 'products')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='shop:product-detail',
        lookup_field='slug'
    )
    tags = TagListSerializerField()
    category = serializers.HyperlinkedRelatedField(
        view_name="shop:category-detail",
        queryset=Category.objects.all(),
        lookup_field='slug'
    )
    images = ProductImageSerializer(read_only=True, many=True)
    reviews = serializers.HyperlinkedIdentityField(
        view_name='shop:review-detail',
        read_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = (
            'url', 'category', 'name', 'slug', 'image',
            'description', 'additional_info', 'price', 'updated',
            'rating', 'tags',
            'images', 'reviews'
        )

    def to_representation(self, instance):
        dictionary = super().to_representation(instance)
        reviews_urls = dictionary.pop('reviews')
        reviews = {
            "reviews": {
                "count": len(reviews_urls),
                "average_rating": self.get_average_rating(instance),
                "urls": reviews_urls
            }
        }
        category_url = dictionary.pop('category')
        category = {
            'category': {
                'url': category_url,
                'name': instance.category.name
            }
        }
        dictionary.update(reviews)
        dictionary.update(category)
        return dictionary

    def get_average_rating(self, instance):
        _avg = Review.objects.filter(product=instance).aggregate(
            Avg('rating')
        )['rating__avg']
        return _avg or 0


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='shop:review-detail')
    author = serializers.SerializerMethodField()
    product = serializers.HyperlinkedRelatedField(
        view_name='shop:product-detail',
        queryset=Product.objects.all(), lookup_field='slug'
    )

    class Meta:
        model = Review
        fields = ('url', 'author', 'product', 'rating', 'created', 'review')

    def get_author(self, instance):
        return {
            'name': instance.user.get_full_name(),
            "image": self.context.get("request").build_absolute_uri(
                instance.user.profile.image.url
            ) if instance.user.profile.image else None,
        }
