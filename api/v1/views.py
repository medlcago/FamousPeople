from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from people.models import Celebrity
from .serializers import UserSerializer, CelebritySerializer


class GetUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CelebrityListAPIView(ListAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
