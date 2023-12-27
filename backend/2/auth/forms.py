from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Username",
            }
        )
    )
    email = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Email",
            }
        )
    )
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Confirm Password",
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Username",
            }
        ),
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
                "placeholder": "Password",
            }
        )
    )
