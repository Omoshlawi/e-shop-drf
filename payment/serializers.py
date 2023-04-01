from rest_framework import serializers

from payment.models import Payment, Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField('payment:transaction-detail')
    payment = serializers.HyperlinkedIdentityField(
        view_name='payment:transaction-detail',
    )
    transaction_id = serializers.SerializerMethodField()

    def get_transaction_id(self, obj):
        return obj.get_transaction_id()

    class Meta:
        model = Transaction
        fields = (
            'url', 'transaction_id', 'payment', 'merchant_request_id', 'checkout_request_id',
            'result_code', 'result_description', 'mpesa_receipt_number',
            'transaction_date', 'phone_number', 'amount', 'created'
        )


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField('payment:payment-detail')
    order = serializers.HyperlinkedIdentityField(view_name='order:order-detail')
    # transactions = serializers.HyperlinkedIdentityField(
    #     view_name='payment:transaction-detail',
    #     many=True
    # )
    payment_id = serializers.SerializerMethodField()
    transactions = TransactionSerializer(many=True)
    balance = serializers.SerializerMethodField()
    amount_paid = serializers.SerializerMethodField()
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = (
            'url', 'payment_id', 'order', 'transactions', 'total_cost',
            'amount_paid', 'balance', 'completed', 'created'
        )

    def get_payment_id(self, obj):
        return obj.get_payment_id()

    def get_balance(self, obj):
        return obj.order.get_balance()

    def get_amount_paid(self, obj):
        return obj.order.get_amount_paid()

    def get_total_cost(self, obj):
        return obj.order.get_total_cost()

    def to_representation(self, instance):
        dictionary = super().to_representation(instance)
        order_url = dictionary.pop("order")
        order_dict = {
            "order": {
                "url": order_url,
                "order": instance.order.get_order_id()
            }
        }
        dictionary.update(order_dict)
        return dictionary
