from django.apps import AppConfig


class PeopleConfig(AppConfig):
    verbose_name = "Знаменитые люди"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'people'
