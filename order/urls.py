from order.views import OrderViewSet, OrderItemViewSet

app_name = "order"
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('items', OrderItemViewSet, basename='item')
router.register('', OrderViewSet, basename='order')

urlpatterns = router.urls