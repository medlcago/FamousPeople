from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("profile/", login_required(views.ProfileView.as_view(), login_url="users:login"), name="profile"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("logout/", views.user_logout, name="logout")
]
