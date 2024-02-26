from django.views.generic import ListView

from .models import Celebrity


# Create your views here.
class MainPageView(ListView):
    model = Celebrity
    template_name = "people/main_page.html"
    context_object_name = "data"
    allow_empty = False

    def get_queryset(self) -> Celebrity:
        return Celebrity.published.all().select_related("category")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = "Знаменитые люди"
        return context
