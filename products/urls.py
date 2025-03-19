from django.urls import path
from products.views import ListProductView


urlpatterns = [
    path("products/", ListProductView.as_view(), name="products"),
]
