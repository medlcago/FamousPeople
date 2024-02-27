from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from .forms import LoginForm
from .mixins import DataMixin
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


class ProfileView(DataMixin, TemplateView):
    template_name = "people/profile.html"
    title = "Профиль"
    is_profile_page = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.title} | {self.request.user.username}"
        return context


def user_logout(request):
    logout(request)
    return redirect("main-page")


class UserLoginView(DataMixin, LoginView):
    login_button = False
    registration_button = True
    main_page_button = True
    template_name = "people/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")
