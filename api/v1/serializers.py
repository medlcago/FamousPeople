from django.contrib.auth import get_user_model
from rest_framework import serializers

from people.models import Celebrity

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source="profile.avatar")

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "avatar"]


class CelebritySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Celebrity
        fields = ["id", "title", "category", "content"]
