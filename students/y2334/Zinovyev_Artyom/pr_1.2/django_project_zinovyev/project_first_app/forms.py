from django import forms
from .models import AutoOwner

class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = AutoOwner
        fields = [
            "name",
            "last_name",
            "birthday_date"
        ]

