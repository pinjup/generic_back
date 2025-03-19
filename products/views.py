# from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class ListProductView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class DetailProductView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()