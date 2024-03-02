from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            return
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return
        return user if self.user_can_authenticate(user) else None

    def user_can_authenticate(self, user):
        return getattr(user, "is_active", True)
