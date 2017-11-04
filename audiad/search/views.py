from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import SearchForm
from .models import Search


class SearchList(ListView):
    model = Search
    paginate_by = 20


class SearchCreate(CreateView):
    model = Search
    form_class = SearchForm
    success_url = reverse_lazy('search:list')


class SearchDetail(DetailView):
    model = Search


class SearchUpdate(UpdateView):
    model = Search
    form_class = SearchForm
    success_url = reverse_lazy('search:list')


class SearchDelete(DeleteView):
    model = Search
    success_url = reverse_lazy('search:list')
