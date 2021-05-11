from django import forms
from . import models

class CreateOwnerForm(forms.ModelForm):
    class Meta:
        model = models.CarOwner

        fields = [
                    'username',
                    'password',
                    'first_name',
                    'last_name',
                    'birthday',
                    'pasport_number',
                    'home_address',
                    'nation',
                ]

