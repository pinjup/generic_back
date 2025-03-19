from rest_framework.routers import DefaultRouter
from categories.viewsets import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)


urlpatterns = router.urls
