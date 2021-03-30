from django import forms
from .models import CarOwner
from UP_project.settings import AUTH_USER_MODEL

class CarOwnerForm (forms.ModelForm):
    class Meta:
        model=CarOwner
        fields=['last_name','first_name','birth_date','passport','nationality','address']