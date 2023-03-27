from rest_framework import serializers

from payment.models import Payment, Transaction


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField('payment:payment-detail')
    order = serializers.HyperlinkedIdentityField(view_name='order:order-detail')
    transactions = serializers.HyperlinkedIdentityField(
        view_name='payment:transaction-detail',
        many=True
    )

    class Meta:
        model = Payment
        fields = ('url', 'order', 'transactions', 'completed', 'created')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField('payment:transaction-detail')
    payment = serializers.HyperlinkedIdentityField(
        view_name='payment:transaction-detail',
    )

    class Meta:
        model = Transaction
        fields = (
            'url', 'payment', 'merchant_request_id', 'checkout_request_id',
            'result_code', 'result_description', 'mpesa_receipt_number',
            'transaction_date', 'phone_number', 'amount', 'created'
        )
