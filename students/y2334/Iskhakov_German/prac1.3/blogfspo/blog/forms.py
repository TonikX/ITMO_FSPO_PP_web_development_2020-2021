from django import forms
from .models import autoOwner
  
  
# creating a form
class ExampleForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = autoOwner
  
        # specify fields to be used
        fields = [
            "last_name",
            "first_name",
            "birth_date"
        ]