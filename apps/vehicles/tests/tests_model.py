from django.test import TestCase

from apps.vehicles.models import Vehicle


# Create your tests here.

class VehicleTestClass(TestCase):
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

    def test_can_drive_1(self):
        country = Vehicle.objects.get(pk=1)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_2(self):
        country = Vehicle.objects.get(pk=2)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_3(self):
        country = Vehicle.objects.get(pk=3)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_4(self):
        country = Vehicle.objects.get(pk=4)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_5(self):
        country = Vehicle.objects.get(pk=5)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_6(self):
        country = Vehicle.objects.get(pk=6)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_7(self):
        country = Vehicle.objects.get(pk=7)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_8(self):
        country = Vehicle.objects.get(pk=8)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_9(self):
        country = Vehicle.objects.get(pk=9)
        self.assertEqual(country.can_drive, False)
