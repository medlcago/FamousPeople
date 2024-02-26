from datetime import datetime

from django.db import models
from django_extensions.db.fields import AutoSlugField
from uuslug import slugify


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
