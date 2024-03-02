from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.fields import AutoSlugField
from uuslug import slugify

from .utils import get_photo_upload_path, get_avatar_upload_path

User = get_user_model()


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Celebrity.Status.PUBLISHED)


class Celebrity(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, "Черновик")
        PUBLISHED = (1, "Опубликовано")

    title: str = models.CharField(max_length=64, unique=True, verbose_name="Заголовок")
    content: str = models.TextField(blank=True, verbose_name="Описание")
    created_at: datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at: datetime = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    is_published: bool = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                             default=Status.DRAFT, verbose_name="Статус")
    slug: str = AutoSlugField(max_length=255, unique=True, db_index=True, populate_from='title',
                              slugify_function=slugify)
    photo: models.ImageField = models.ImageField(upload_to=get_photo_upload_path, default=None, blank=True, null=True,
                                                 verbose_name="Фото")
    category: "Category" = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts",
                                             verbose_name="Категория")

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Знаменитость"
        verbose_name_plural = "Знаменитости"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Deleting the previous photo when updating an object
        if self.pk:
            old_instance = Celebrity.objects.get(pk=self.pk)
            if old_instance.photo and self.photo != old_instance.photo:
                old_instance.photo.delete(save=False)
        super().save(*args, **kwargs)


class Category(models.Model):
    name: str = models.CharField(unique=True, max_length=255, db_index=True, verbose_name="Категория")
    slug: str = AutoSlugField(max_length=255, unique=True, db_index=True, populate_from='name',
                              slugify_function=slugify)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("pk",)

    def __str__(self):
        return self.name


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
        Profile.objects.create(user=instance)
