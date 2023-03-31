from django.contrib.auth.models import User
from rest_framework import serializers

from order.models import Order, OrderItem
from shop.models import Product


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order:item-detail')
    order = serializers.HyperlinkedRelatedField(
        view_name='order:order-detail',
        read_only=True
    )
    product = serializers.HyperlinkedRelatedField(
        view_name='shop:product-detail',
        lookup_field='slug',
        queryset=Product.objects.filter(available=True)
    )
    price = serializers.DecimalField(read_only=True, max_digits=12, decimal_places=2)
    total_cost = serializers.SerializerMethodField()

    def get_total_cost(self, obj):
        return obj.get_cost()

    def to_representation(self, instance):
        dictionary = super().to_representation(instance)
        url = dictionary.pop('product')
        product = {
            'product': {
                'url': url,
                'name': instance.product.name,
                "image": self.context.get("request").build_absolute_uri(
                    instance.product.image.url) if instance.product.image else None,
                "category": instance.product.category.name
            }
        }
        dictionary.update(product)
        return dictionary

    class Meta:
        model = OrderItem
        fields = (
            'url', 'order', 'price',
            'quantity',
            'total_cost',
            'product'
        )


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order:order-detail')
    user = serializers.HyperlinkedRelatedField(
        view_name='users:user-detail',
        # queryset=User.objects.all()
        read_only=True
    )
    items = OrderItemSerializer(many=True)
    order_id = serializers.SerializerMethodField()
    total_cost = serializers.SerializerMethodField(method_name='get_total')
    paid = serializers.SerializerMethodField(method_name='get_paid')
    amount_paid = serializers.SerializerMethodField(method_name='get_amount_paid')
    balance = serializers.SerializerMethodField(method_name='get_balance')

    def get_order_id(self, obj):
        return f"ORD-{obj.id}-{obj.created.year}"

    def get_total(self, obj):
        return obj.get_total_cost()

    def get_paid(self, obj):
        return obj.paid

    def get_amount_paid(self, obj):
        return obj.get_amount_paid()

    def get_balance(self, obj):
        return obj.get_balance()

    def create(self, validated_data):
        user = self.context.get('request').user
        order = Order.objects.create(user=user)
        items = validated_data.pop("items")
        if items:
            for item in items:
                OrderItem.objects.create(order=order, price=item['product'].price, **item)
        return order

    class Meta:
        model = Order
        fields = (
            'order_id',
            'url', 'user', 'items',
            'created', 'updated',
            'total_cost', 'paid',
            'amount_paid', 'balance'
        )

# class OrderAddSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ("product", "price", "quantity")
