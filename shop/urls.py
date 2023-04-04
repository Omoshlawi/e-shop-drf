from shop.views import CategoryViewSet, ProductViewSet, ReviewViewSet, TagsViewSet
from django.urls import path

app_name = "shop"
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("categories", CategoryViewSet, 'category')
router.register("reviews", ReviewViewSet, 'review')
router.register("tags", TagsViewSet, 'tag')
router.register("", ProductViewSet, 'product')

urlpatterns = router.urls
