from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = "api"

urlpatterns = [
    path("getme/", views.GetUserView().as_view(), name="getme"),
    path("posts/", views.CelebrityListAPIView().as_view(), name="posts"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify")
]
