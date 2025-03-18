# from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.
class ListCategoryView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()