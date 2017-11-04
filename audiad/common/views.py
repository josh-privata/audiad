from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import LocationForm
from .models import Location


class LocationList(ListView):
    model = Location
    paginate_by = 20


class LocationCreate(CreateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('common:list')


class LocationDetail(DetailView):
    model = Location


class LocationUpdate(UpdateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('common:list')


class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('common:list')
