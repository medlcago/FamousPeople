from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            return
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return
        return user if self.user_can_authenticate(user) else None

    def user_can_authenticate(self, user):
        return getattr(user, "is_active", True)



