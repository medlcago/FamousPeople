from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "avatar")
    list_display_links = ("id", "user")
    search_fields = ("user__username__startswith",)
    list_per_page = 5
    save_on_top = True
