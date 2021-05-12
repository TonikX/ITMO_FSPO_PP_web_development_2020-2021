from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Worker, Wagon, Repair


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "tab_number",
            "fio_worker",
            "year_worker",
            "base_worker",
            "bonus_worker",
            "number_cart_bank",
            "brigade"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class WagonForm(forms.ModelForm):
    class Meta:
        model = Wagon
        fields = [
            "reg_number",
            "reg_name",
            "reg_chief",
            "type",
            "type_year",
            "dop_number",
            "ralway_addressExternal"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            "resalt",
            "reason",
            "cost",
            "day_start",
            "day_stop",
            "type_repair",
            "schedule",
            "wagon"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
