from django.urls import path

from apps.vehicles.views import VehicleListView, VehicleCreateView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list-view'),
    path('vehicle/create', VehicleCreateView.as_view(), name='vehicle-create-view'),
]
