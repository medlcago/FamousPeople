from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите имя пользователя', 'required': True, 'minlength': 4,
             "maxlength": 32})
        self.fields["password"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите пароль', 'required': True, 'minlength': 6})


class RegistrationForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, label="Имя пользователя", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя', 'required': True, 'minlength': 4,
               'maxlength': 32}))
    email = forms.EmailField(required=True, label="Электронная почта", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите адрес электронной почты', 'required': True}))
    password1 = forms.CharField(required=True, min_length=6, label="Пароль", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'required': True, 'minlength': 6}),
                                error_messages={'required': 'Введите пароль',
                                                'min_length': 'Пароль должен содержать минимум 6 символов'})
    password2 = forms.CharField(required=True, min_length=6, label="Подтверждение пароля", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль', 'required': True, 'minlength': 6}),
                                error_messages={'required': 'Подтвердите пароль',
                                                'min_length': 'Пароль должен содержать минимум 6 символов'})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой электронной почтой уже существует")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        user = get_user_model().objects.create_user(username=username, email=email, password=password)
        return user
