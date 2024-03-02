from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.utils import get_avatar_upload_path

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="Профиль")
    avatar = models.ImageField(upload_to=get_avatar_upload_path, default=None, blank=True, null=True,
                               verbose_name="Аватарка")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ("pk",)

    def __str__(self):
        return f"Профиль {self.user}"

    def save(self, *args, **kwargs):
        # Deleting the previous avatar when updating an object
        if self.pk:
            old_instance = Profile.objects.get(pk=self.pk)
            if old_instance.avatar and self.avatar != old_instance.avatar:
                old_instance.avatar.delete(save=False)
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not hasattr(instance, "profile"):
        with transaction.atomic():
            Profile.objects.create(user=instance)
