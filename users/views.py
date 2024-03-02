from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from FamousPeople.mixins import DataMixin
from .forms import (
    LoginForm, RegistrationForm
)


# Create your views here.


class ProfileView(DataMixin, TemplateView):
    template_name = "users/profile.html"
    title = "Профиль"
    is_profile_page = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.title} | {self.request.user.username}"
        return context


def user_logout(request):
    logout(request)
    return redirect("people:main-page")


class UserLoginView(DataMixin, LoginView):
    title = "Авторизация"
    login_button = False
    registration_button = True
    main_page_button = True
    template_name = "users/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("users:profile")


class UserRegistrationView(DataMixin, FormView):
    title = "Регистрация"
    login_button = True
    registration_button = False
    main_page_button = True
    template_name = "users/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().get(request, *args, **kwargs)
