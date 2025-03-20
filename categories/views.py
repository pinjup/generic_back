# from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from categories.models import Category
from categories.serializers import CategorySerializer

# GET api/categories/
# POST api/categories/
class ListCategoryView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# GET api/categories/<id>/
# PUT api/categories/<id>/
# DELETE api/categories/<id>/
class DetailCategoryView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()