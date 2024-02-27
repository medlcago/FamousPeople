class DataMixin:
    title = ""
    is_profile_page = False
    login_button = True
    registration_button = True
    main_page_button = False
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["user"] = self.request.user
        context["is_profile_page"] = self.is_profile_page
        context["login_button"] = self.login_button
        context["registration_button"] = self.registration_button
        context["main_page_button"] = self.main_page_button
        return context
