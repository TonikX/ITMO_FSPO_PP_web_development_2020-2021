from django import forms
from .models import Owner


class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "username",
            "last_name",
            "password",
            "first_name",
            "birth_date",
            "passport_num",
            "nationality",
            "address",
        ]
