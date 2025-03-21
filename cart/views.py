from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer
from products.models import Product


class UserCartAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def verify_user(self, user_id):
        if self.request.user.is_staff:
            return True
        return int(user_id) == self.request.user.id

    def get_cart(self, user_id):
        if self.request.user.is_staff:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return None
        else:
            user = self.request.user
        return user.cart

    def get(self, request, user_id, *args, **kwargs):
        if not self.verify_user(user_id):
            return Response(
                {"detail": "Access denied."}, status=status.HTTP_403_FORBIDDEN
            )
        cart = self.get_cart(user_id)
        if cart is None:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        cart_items = cart.items.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        if not self.verify_user(user_id):
            return Response(
                {"detail": "Access denied."}, status=status.HTTP_403_FORBIDDEN
            )

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
                {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

        cart = self.get_cart(user_id)
        if cart is None:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            requested_qty = int(quantity)
        except ValueError:
            return Response(
                {"detail": "Quantity must be a valid number."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if requested_qty > product.stock:
            return Response(
                {"detail": "Requested quantity exceeds available stock."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": requested_qty}
        )
        if not created:
            new_qty = cart_item.quantity + requested_qty
            if new_qty > product.stock:
                return Response(
                    {"detail": "Total quantity in cart exceeds available stock."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            cart_item.quantity = new_qty
            cart_item.save()

        cart_items = cart.items.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
