from django.urls import path
from store import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'product_list', views.ProductListViewSet)
# router.register(r'product_items', views.ProductItemViewSet)

urlpatterns = router.urls
