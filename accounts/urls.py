from django.urls import path
from accounts.views import (
    LoginAPIView,
    UserListView,
    UserProfileListView,
    UserProfileDetailView,
    UserRegistrationView,
    LogoutAPIView,
    SizeListView,
    SizeDetailView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profiles/", UserProfileListView.as_view(), name="profile-list"),
    path("profile/", UserProfileDetailView.as_view(), name="profile-detail"),
    path("sizes/", SizeListView.as_view(), name="size-list"),
    path("sizes/<int:pk>/", SizeDetailView.as_view(), name="size-detail"),
]
