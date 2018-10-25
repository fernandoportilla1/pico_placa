from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.vehicles.forms import VehicleForm
from apps.vehicles.models import Vehicle


# Create your views here.
class VehicleListView(ListView):
    model = Vehicle


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle-list-view')
