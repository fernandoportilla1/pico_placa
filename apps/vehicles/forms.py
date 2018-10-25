from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from apps.vehicles.models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = ['created_at']
        widgets = {
            'license_plate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'current_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'current_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'vehicle-form'
        self.helper.form_class = 'form'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout('license_plate_number', 'current_date', 'current_time')

        self.helper.add_input(Submit('submit-name', 'Save'))
