from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите имя пользователя', 'required': True, 'minlength': 4,
             "maxlength": 32})
        self.fields["password"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите пароль', 'required': True, 'minlength': 6})
