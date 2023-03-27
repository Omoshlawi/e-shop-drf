from shop.views import CategoryViewSet, ProductViewSet
from django.urls import path

app_name = "shop"
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("categories", CategoryViewSet, 'category')
router.register("", ProductViewSet, 'product')

urlpatterns = router.urls
