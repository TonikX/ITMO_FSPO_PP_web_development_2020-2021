from django import forms
from project_first_app.models import Owner


# creating a form
class OwnerForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birth_date",
        ]
