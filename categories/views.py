# from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.
class ListCategoryView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class DetailCategoryView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()