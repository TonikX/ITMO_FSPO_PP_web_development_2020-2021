from django import forms
from .models import AutoOwner


class AutoOwnerForm(forms.ModelForm):

    class Meta:
        model = AutoOwner

        fields = [
            "last_name",
            "name",
            "birthday_date"
        ]
