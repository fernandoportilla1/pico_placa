from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.vehicles.forms import VehicleForm
from apps.vehicles.models import Vehicle


# Create your views here.
class VehicleListView(ListView):
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_list'] = 'active'
        return context


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_create'] = 'active'
        return context
