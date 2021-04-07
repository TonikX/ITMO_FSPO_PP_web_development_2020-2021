from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Owner


class add_owner_form(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "pass_num",
            "address",
            "nationality",
        ]


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('id', 'password')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('id', 'password')
