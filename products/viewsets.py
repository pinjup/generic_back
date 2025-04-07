from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer
from accounts.permissions import IsAdminUser

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_permissions(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]