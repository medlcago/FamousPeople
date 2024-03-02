from django.db import models
from django_extensions.db.fields import AutoSlugField
from uuslug import slugify


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
