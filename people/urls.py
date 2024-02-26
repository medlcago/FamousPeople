from . import views
from django.urls import path

urlpatterns = [
    path("main/", views.MainPageView.as_view(), name="main_page"),
]
