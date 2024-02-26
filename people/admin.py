from django.contrib import admin
from uuslug import slugify

from .models import (
    Celebrity, Category
)


# Register your models here.

@admin.register(Celebrity)
class CelebritiesAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    list_display = ("id", "title", "content", "created_at", "updated_at", "is_published", "slug", "category")
    list_display_links = ("id", "title")
    search_fields = ("title__startswith",)
    list_editable = ("is_published",)
    list_per_page = 5
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if change:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]
    list_display = ("id", "name", "slug")
    list_display_links = ("id",)
    search_fields = ("name__startswith",)
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if change:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
