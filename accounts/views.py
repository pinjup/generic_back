from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsAdminUser
from accounts.models import UserProfile, Size
from accounts.serializers import (
    UserRegistrationSerializer,
    UserListSerializer,
    UserProfileSerializer,
    SizeSerializer,
)

User = get_user_model()


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Both username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(
                {"detail": "Credentials are valid."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"detail": "Logged out successfully."}, status=status.HTTP_200_OK
        )


class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserProfileDetailView(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile


class SizeListView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def get_authentication_classes(self):
        if self.request.method == "POST":
            return [TokenAuthentication]
        return []

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]


class SizeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def get_authentication_classes(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [TokenAuthentication]
        return []

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]
