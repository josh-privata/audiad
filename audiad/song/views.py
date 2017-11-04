from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import SongForm
from .models import Song


class SongList(ListView):
    model = Song
    paginate_by = 20


class SongCreate(CreateView):
    model = Song
    form_class = SongForm
    success_url = reverse_lazy('song:list')


class SongDetail(DetailView):
    model = Song


class SongUpdate(UpdateView):
    model = Song
    form_class = SongForm
    success_url = reverse_lazy('song:list')


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song:list')
