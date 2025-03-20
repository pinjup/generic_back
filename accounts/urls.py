from django.urls import path
from accounts.views import UserListView, UserRegistrationView

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='user-registration'),
    path("users/", UserListView.as_view(), name="user-list"),
]