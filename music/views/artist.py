from digg_paginator import DiggPaginator as Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from music.tables import ArtistTable
from music.forms import ArtistForm
from music.models import Album, Artist, Song


class Artists(View):

    def get(self, request, filter_by='all'):
        if not request.user.is_authenticated():
            return render(request, 'music/auth/login.html')
        else:
            page = request.GET.get('page', 1)
            try:
                artist_ids = []
                artists = []
                for artist in Artist.objects.all():
                    artist_ids.append(artist.pk)
                    artists = Artist.objects.filter(pk__in=artist_ids)
                if filter_by == 'favorites':
                    artists = artists.filter(fav=True)
                paginate_artists = Paginator(artists, 20, body=3, margin=1, tail=1)
                try:
                    artists = paginate_artists.page(page)
                except PageNotAnInteger:
                    artists = paginate_artists.page(1)
                except EmptyPage:
                    artists = paginate_artists.page(paginate_artists.num_pages)
            except Artist.DoesNotExist:
                artists = []
            return render(request, 'music/artist/artists.html', {
                'artist_list': artists,
                'filter_by': filter_by,
            })


class ArtistDetailView(DetailView):

    template_name = 'music/artist/artist_detail.html'
    model = Artist

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            user = self.request.user
            artists = Artist.objects.all()
            songs = Song.objects.all()
            albums = Album.objects.all()
            genre = ""
            artist = self.object
            context = super(ArtistDetailView, self).get_context_data(**kwargs)
            context['artist'] = artist
            context['user'] = user
            if self.object.genre.name:
                genre = self.object.genre.name
            context['similar_artist'] = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=artist.name)[:5]
            context['similar_albums'] = albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(artist=artist.id)[:5]
            context['similar_song'] = songs.filter(Q(genre__name__icontains=genre)).distinct().exclude(artist=artist.id).distinct()[:5]
            return context


class ArtistUpdate(UpdateView):

    model = Artist
    form_class = ArtistForm
    template_name = 'music/artist/artist_update.html'

    def form_valid(self, form):
        artist = form.save(commit=False)
        artist.user = self.request.user
        artist.save()
        return super(ArtistUpdate, self).form_valid(form)


class ArtistDelete(DeleteView):

    model = Artist
    success_url = reverse_lazy('music:artists_list')
    template_name_suffix = '_delete'
    template_name = 'music/artist/artist_delete.html'


class ArtistCreate(CreateView):

    model = Artist
    form_class = ArtistForm
    template_name = 'music/artist/artist_create.html'

    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            artist = form.save(commit=False)
            artist.user = self.request.user
            artist.save()


class ArtistView(FormView):

    template_name = 'music/artist/artist_create.html'
    form_class = ArtistForm
    success_url = '/index/'

    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            artist = form.save(commit=False)
            artist.user = self.request.user
            artist.save()
            return super(ArtistView, self).form_valid(form)


class ArtistList(ListView):

    template_name = 'music/artist/artist_table.html'
    model = Artist

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            user = self.request.user
            context = super(ArtistList, self).get_context_data(**kwargs)
            table = ArtistTable(Artist.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


def fav_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if artist.fav:
        artist.fav = False
    else:
        artist.fav = True
        artist.save()
    artists = Artist.objects.all()
    return render(request, 'music/artist/artists.html', {'artists': artists})