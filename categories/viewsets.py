from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.models import Category
from products.models import Product
from categories.serializers import CategorySerializer
from products.serializers import ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    @action(
        ["GET", "POST"],
        detail=True,
        serializer_class=ProductSerializer,
    )
    def products(self, request, pk):
        category = self.get_object()
        
        if request.method == "GET":
            products = Product.objects.filter(category_id=category.id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            data = request.data.copy()
            data["category"] = category.id
            serializer = ProductSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(["GET", "DELETE", "PUT", "PATCH"], detail=True, serializer_class=ProductSerializer, url_path="products/(?P<product_id>[^/.]+)")
    def detail_products(self, request, pk, product_id=None):
        category = self.get_object()
        try:
            product = Product.objects.get(id=product_id, category=category.id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == "GET":
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        if request.method == "DELETE":
            serializer = ProductSerializer(product)
            product.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        
        if request.method == "PUT":
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == "PATCH":
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)