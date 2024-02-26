class DataMixin:
    title = ""
    is_profile_page = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["user"] = self.request.user
        context["is_profile_page"] = self.is_profile_page
        return context
