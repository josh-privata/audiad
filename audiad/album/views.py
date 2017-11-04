from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AlbumForm
from .models import Album


class AlbumList(ListView):
    model = Album
    paginate_by = 20


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('album:list')


class AlbumDetail(DetailView):
    model = Album


class AlbumUpdate(UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('album:list')


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album:list')
