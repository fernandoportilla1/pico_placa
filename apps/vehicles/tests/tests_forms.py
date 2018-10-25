from django.test import TestCase

from apps.vehicles.forms import VehicleForm


# Create your tests here.


class VehicleTestClass(TestCase):
    def test_license_plate_number_field_label(self):
        form = VehicleForm()
        self.assertEquals(form.fields['license_plate_number'].label, 'License Plate Number')

    def test_current_date_field_label(self):
        form = VehicleForm()
        self.assertEquals(form.fields['current_date'].label, 'Current Date')

    def test_current_time_field_label(self):
        form = VehicleForm()
        self.assertEquals(form.fields['current_time'].label, 'Current Time')
