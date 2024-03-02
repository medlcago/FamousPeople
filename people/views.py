from django.views.generic import ListView

from FamousPeople.mixins import DataMixin
from .models import Celebrity


# Create your views here.
class MainPageView(DataMixin, ListView):
    model = Celebrity
    template_name = "people/main-page.html"
    context_object_name = "data"
    allow_empty = False
    title = "Знаменитые люди"

    def get_queryset(self) -> Celebrity:
        return Celebrity.published.all().select_related("category")
