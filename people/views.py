from django.views.generic import ListView, TemplateView

from .mixins import DataMixin
from .models import Celebrity


# Create your views here.
class MainPageView(DataMixin, ListView):
    model = Celebrity
    template_name = "people/main_page.html"
    context_object_name = "data"
    allow_empty = False
    title = "Знаменитые люди"

    def get_queryset(self) -> Celebrity:
        return Celebrity.published.all().select_related("category")


class ProfileView(DataMixin, TemplateView):
    template_name = "people/profile.html"
    title = "Профиль"
    is_profile_page = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.title} | {self.request.user.username}"
        return context
