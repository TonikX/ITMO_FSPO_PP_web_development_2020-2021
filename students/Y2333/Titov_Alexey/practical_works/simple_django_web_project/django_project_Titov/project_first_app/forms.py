from django import forms
from .models import Owner


class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "surname",
            "name",
            "birth_date",
        ]


