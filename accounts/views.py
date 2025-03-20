from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from accounts.serializers import UserRegistrationSerializer, UserListSerializer

User = get_user_model()
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated] 
