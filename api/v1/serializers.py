from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from people.models import Celebrity

User = get_user_model()


class JWTTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["token"] = data.pop("access")
        data["refresh_token"] = data.pop("refresh")
        token = self.get_token(self.user)
        data["lifetime"] = token["exp"] - token["iat"]
        return data


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source="profile.avatar")

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "avatar"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data["avatar"] is None:
            del data["avatar"]
        return data


class CelebritySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Celebrity
        fields = ["id", "title", "category", "content"]
