from django.urls import path

from apps.vehicles.views import VehicleListView, VehicleCreateView

urlpatterns = [
    path('vehicle', VehicleListView.as_view(), name='vehicle-list-view'),
    path('vehicle/create', VehicleCreateView.as_view(), name='vehicle-create-view'),
]
