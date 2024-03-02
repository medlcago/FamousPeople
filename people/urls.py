from django.urls import path

from . import views

app_name = "people"

urlpatterns = [
    path("main/", views.MainPageView.as_view(), name="main-page")
]
