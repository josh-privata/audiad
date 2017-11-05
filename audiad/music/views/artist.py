"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from digg_paginator import DiggPaginator as Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView, View
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from music.tables import ArtistTable as AT
from music.forms import ArtistForm
from music.models import Album, Artist, Song


class Artists(View):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    def get(self, request, filter_by='all'):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
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
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/artist/artist_detail.html'
    model = Artist

    def get_context_data(self, **kwargs):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
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
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    # todo Doesnt populate fields
    model = Artist
    form_class = ArtistForm
    template_name = 'music/artist/artist_update.html'

    def form_valid(self, form):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
        artist = form.save(commit=False)
        artist.user = self.request.user
        artist.save()
        return super(ArtistUpdate, self).form_valid(form)


class ArtistDelete(DeleteView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Artist
    success_url = reverse_lazy('music:artists_list')
    template_name_suffix = '_delete'
    template_name = 'music/artist/artist_delete.html'


class ArtistCreate(CreateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Artist
    form_class = ArtistForm
    template_name = 'music/artist/artist_create.html'

    def form_valid(self, form):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            artist = form.save(commit=False)
            artist.user = self.request.user
            artist.save()


class ArtistView(FormView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/artist/artist_create.html'
    form_class = ArtistForm
    success_url = '/index/'

    def form_valid(self, form):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            artist = form.save(commit=False)
            artist.user = self.request.user
            artist.save()
            return super(ArtistView, self).form_valid(form)


class ArtistTable(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/artist/artist_table.html'
    model = Artist

    def get_context_data(self, **kwargs):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            user = self.request.user
            context = super(ArtistTable, self).get_context_data(**kwargs)
            table = AT(Artist.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


class ArtistList(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    def get(self, request, filter_by='all'):
        """docstring

                Note:
                    Do not include the `self` parameter in the ``Args`` section.

                Args:
                    param1: The first parameter.
                    param2: The second parameter.

                Returns:
                    True if successful, False otherwise.

                """
        # todo Finish docstring
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
            return render(request, 'music/artist/artist_list.html', {
                'artist_list': artists,
                'filter_by': filter_by,
            })


def fav_artist(request, artist_id):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    artist = get_object_or_404(Artist, pk=artist_id)
    if artist.fav:
        artist.fav = False
    else:
        artist.fav = True
        artist.save()
    artists = Artist.objects.all()
    return render(request, 'music/artist/artists.html', {'artists': artists})