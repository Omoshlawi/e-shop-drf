from rest_framework.routers import DefaultRouter

from payment.views import TransactionViewSet, PaymentViewSet

app_name = "payment"

router = DefaultRouter()
router.register('transactions', TransactionViewSet, 'transaction')
router.register('', PaymentViewSet, 'payment')

urlpatterns = router.urls
