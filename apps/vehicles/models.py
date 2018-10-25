from datetime import datetime, time

from django.db import models
from django.utils.timezone import now


# Create your models here.

class Vehicle(models.Model):
    license_plate_number = models.CharField('License Plate Number', max_length=10)
    current_date = models.DateField('Current Date')
    current_time = models.TimeField('Current Time')
    created_at = models.DateTimeField('Created at', default=now, blank=True)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.license_plate_number

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        super(Vehicle, self).save(*args, **kwargs)

    @property
    def can_drive(self):
        weekday = datetime.strptime(str(self.current_date), "%Y-%m-%d").weekday()
        current_time = self.current_time
        checker = self.license_plate_number[-1]

        if time(7, 00, 00) <= current_time <= time(9, 30, 00) or time(14, 00, 00) <= current_time <= time(19, 30, 00):
            if weekday == 0 and (checker == '1' or checker == '2'):
                return True
            if weekday == 1 and (checker == '3' or checker == '4'):
                return True
            if weekday == 2 and (checker == '5' or checker == '6'):
                return True
            if weekday == 3 and (checker == '7' or checker == '8'):
                return True
            if weekday == 4 and (checker == '9' or checker == '0'):
                return True
        return False
