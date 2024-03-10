from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from people.models import Celebrity
from .serializers import UserSerializer, CelebritySerializer, JWTTokenObtainPairSerializer


class JWTTokenObtainPairView(TokenObtainPairView):
    serializer_class = JWTTokenObtainPairSerializer


class GetUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CelebrityListAPIView(ListAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
