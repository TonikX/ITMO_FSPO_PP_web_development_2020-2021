from django import forms
from .models import owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = owner

        fields = [
                "name",
                "last_name",
                "borndate",
                ]
