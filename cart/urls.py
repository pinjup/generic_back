from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.views import UserCartAPIView


urlpatterns = [
    path('cart/<int:user_id>', UserCartAPIView.as_view(), name='user-cart'),
]