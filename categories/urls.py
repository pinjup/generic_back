from django.urls import path
from categories.views import ListCategoryView


urlpatterns = [
    path("categories/", ListCategoryView.as_view(), name="categories"),
]
