from django.urls import path
from categories.views import ListCategoryView
from rest_framework.routers import DefaultRouter
from categories.viewsets import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)


urlpatterns = [
    # path("categories/", ListCategoryView.as_view(), name="categories"),
] + router.urls
