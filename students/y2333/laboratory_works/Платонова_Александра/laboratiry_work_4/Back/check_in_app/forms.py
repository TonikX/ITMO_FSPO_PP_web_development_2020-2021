from django import forms
from .models import Payment

class PayForm(forms.ModelForm):
    class Meta:
        model = Payment

        fields = [
            "amount",
            "status",
            "date_pay",
            "check_in_out_id",
        ]