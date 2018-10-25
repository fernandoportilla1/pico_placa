from django.test import TestCase
# Create your tests here.
from django.urls import reverse

from apps.vehicles.models import Vehicle


class CompanyTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='7:00:00')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='9:30:00')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='6:59:59')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='9:30:01')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='14:00:00')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='19:30:00')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='13:59:59')
        Vehicle.objects.create(license_plate_number="PAC-121", current_date='2018-10-22', current_time='19:30:01')
        Vehicle.objects.create(license_plate_number="PAC-123", current_date='2018-10-22', current_time='7:00:00')

    def test_view_url_exists(self):
        url = '/vehicle'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_return_all_entries(self):
        url = '/vehicle'
        response = self.client.get(url)
        self.assertEqual(response.context['vehicle_list'].count(), Vehicle.objects.all().count())

    def test_template_list(self):
        response = self.client.get(reverse('vehicle-list-view'))
        self.assertTemplateUsed(response, 'vehicles/vehicle_list.html')

    def test_template_create(self):
        response = self.client.get(reverse('vehicle-create-view'))
        self.assertTemplateUsed(response, 'vehicles/vehicle_form.html')
