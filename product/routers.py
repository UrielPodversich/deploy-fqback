from rest_framework import routers
from product.views import ProductViewSet # noqa

router = routers.DefaultRouter()
router.register('', ProductViewSet, basename='products')

urlpatterns = router.urls
