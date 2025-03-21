from django.urls import path
from accounts.views import LoginAPIView, UserListView, UserRegistrationView

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='user-registration'),
    path("users/", UserListView.as_view(), name="user-list"),
    path("login/", LoginAPIView.as_view(), name="login"),
]