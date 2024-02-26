from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.MainPageView.as_view(), name="main_page"),
    path("profile/", views.ProfileView.as_view(), name="profile")
]
