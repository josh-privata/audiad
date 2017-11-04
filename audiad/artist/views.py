from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ArtistForm
from .models import Artist


class ArtistList(ListView):
    model = Artist
    paginate_by = 20


class ArtistCreate(CreateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy('artist:list')


class ArtistDetail(DetailView):
    model = Artist


class ArtistUpdate(UpdateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy('artist:list')


class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('artist:list')
