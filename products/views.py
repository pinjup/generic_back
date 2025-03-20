# from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from products.models import Product
from products.serializers import ProductSerializer

# GET api/products/
# POST api/products/
class ListProductView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# GET api/products/<id>/
# PUT api/products/<id>/
# DELETE api/products/<id>/
class DetailProductView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()