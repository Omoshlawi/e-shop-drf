from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from payment.models import Payment, Transaction
from payment.serializers import PaymentSerializer, TransactionSerializer


# Create your views here.


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(order__user=self.request.user)


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    permissions = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(payment__order__user=self.request.user)
