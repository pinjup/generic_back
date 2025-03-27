from django.urls import path
from accounts.views import (
    LoginAPIView,
    UserListView,
    UserProfileListView,
    UserRegistrationView,
    LogoutAPIView,
)

urlpatterns = [
    path(
        "accounts/register/", UserRegistrationView.as_view(), name="user-registration"
    ),
    path("users/", UserListView.as_view(), name="user-list"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profiles/", UserProfileListView.as_view(), name="profile-list"),
]
