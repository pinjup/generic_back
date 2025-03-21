from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from cart.models import CartItem
from cart.serializers import CartItemSerializer
from products.models import Product

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user(self):
        # Se espera que la URL incluya el parámetro 'user_id'
        user_id = self.kwargs.get("user_id")
        if user_id is None:
            raise PermissionDenied("User ID is required in URL.")
        if int(user_id) != self.request.user.id:
            raise PermissionDenied("You are not allowed to access this cart.")
        return self.request.user

    def get_queryset(self):
        user = self.get_user()
        return CartItem.objects.filter(cart=user.cart)

    def create(self, request, *args, **kwargs):
        user = self.get_user()
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        if not product_id:
            return Response(
                {"detail": "Product ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        cart = user.cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Permite modificar únicamente la cantidad del ítem
        self.get_user()  # Se verifica el usuario
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if "quantity" not in request.data:
            return Response(
                {"detail": "Quantity is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance.quantity = request.data.get("quantity")
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
