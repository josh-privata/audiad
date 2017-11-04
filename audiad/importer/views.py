from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ImporterForm
from .models import Importer


class ImporterList(ListView):
    model = Importer
    paginate_by = 20


class ImporterCreate(CreateView):
    model = Importer
    form_class = ImporterForm
    success_url = reverse_lazy('importer:list')


class ImporterDetail(DetailView):
    model = Importer


class ImporterUpdate(UpdateView):
    model = Importer
    form_class = ImporterForm
    success_url = reverse_lazy('importer:list')


class ImporterDelete(DeleteView):
    model = Importer
    success_url = reverse_lazy('importer:list')
