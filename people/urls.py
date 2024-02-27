from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.MainPageView.as_view(), name="main-page"),
    path("profile/", login_required(views.ProfileView.as_view(), login_url="login"), name="profile"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout")
]
