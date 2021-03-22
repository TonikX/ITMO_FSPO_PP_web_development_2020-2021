from django import forms
from .models import Owner



class add_owner_form(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "id",
            "last_name",
            "first_name",
            "birthdate",
        ]
