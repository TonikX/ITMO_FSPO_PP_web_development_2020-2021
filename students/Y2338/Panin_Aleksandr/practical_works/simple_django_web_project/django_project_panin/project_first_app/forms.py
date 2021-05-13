from django import forms
from .models import CarOwner


class CarOwnerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }

    class Meta:
        model = CarOwner
        fields = [
            "username",
            "password",
            "surname",
            "name",
            "birthday",
            "passport",
            "address",
            "nationality"
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CarOwnerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
