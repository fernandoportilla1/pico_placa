from django.contrib import admin

# Register your models here.
from apps.vehicles.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate_number', 'current_date', 'current_time')
    list_filter = ['license_plate_number']


admin.site.register(Vehicle, VehicleAdmin)
