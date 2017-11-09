"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring
from django.core.urlresolvers import reverse_lazy

from audiad.music.forms import SongForm1
from digg_paginator import DiggPaginator as Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView, View
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from audiad.music.forms import SongForm2, SongForm1
from audiad.music.models import Album, Artist, Song
from audiad.music.tables import SongTable as ST


class Songs(View):
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
                song_ids = []
                for album in Album.objects.filter(user=request.user):
                    for song in album.song_set.all():
                        song_ids.append(song.pk)
                user_songs = Song.objects.filter(pk__in=song_ids)
                if filter_by == 'favorites':
                    user_songs = user_songs.filter(fav=True)
                paginate_songs = Paginator(user_songs, 20, body=3, margin=1, tail=1)
                try:
                    user_songs = paginate_songs.page(page)
                except PageNotAnInteger:
                    user_songs = paginate_songs.page(1)
                except EmptyPage:
                    user_songs = paginate_songs.page(paginate_songs.num_pages)
            except Album.DoesNotExist:
                user_songs = []
            return render(request, 'music/song/songs.html', {
                'song_list': user_songs,
                'filter_by': filter_by,
            })


class SongList(ListView):
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
                song_ids = []
                songs = []
                for song in Song.objects.all():
                    song_ids.append(song.pk)
                    songs = Song.objects.filter(pk__in=song_ids)
                if filter_by == 'favorites':
                    songs = songs.filter(fav=True)
                paginate_songs = Paginator(songs, 20, body=3, margin=1, tail=1)
                try:
                    songs = paginate_songs.page(page)
                except PageNotAnInteger:
                    songs = paginate_songs.page(1)
                except EmptyPage:
                    songs = paginate_songs.page(paginate_songs.num_pages)
            except Song.DoesNotExist:
                songs = []
            return render(request, 'music/song/song_list.html', {
                'object_list': songs,
                'filter_by': filter_by,
            })


class SongTable(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/song/songs_table.html'
    model = Song

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
            context = super(SongTable, self).get_context_data(**kwargs)
            table = ST(Song.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


class SongDetailView(DetailView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/song/song_detail.html'
    model = Song

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
            song = self.object
            album = song.album
            genre = ""
            context = super(SongDetailView, self).get_context_data(**kwargs)
            context['song'] = song
            context['user'] = user
            context['album'] = album
            if self.object.genre.name:
                genre = self.object.genre.name
            context['similar_artist'] = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=album.artist)[:5]
            context['similar_song'] = songs.filter(Q(genre__name__icontains=genre)).distinct().exclude(title=album.title)[:5]
            context['similar_song'] = songs.filter(Q(genre__name__icontains=genre)).distinct().exclude(album=album.id)[:5]
            return context


class SongUpdate(UpdateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    # todo Doesnt populate fields
    model = Song
    form_class = SongForm2
    template_name_suffix = '_update'
    template_name = 'music/song/song_update.html'

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
        song = form.save(commit=False)
        song.save()
        return super(SongUpdate, self).form_valid(form)


class SongView(FormView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/song/song_create.html'
    form_class = SongForm2
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
            song = form.save(commit=False)
            song.user = self.request.user
            song.save()
            return super(SongView, self).form_valid(form)


class SongDelete(DeleteView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Song
    form_class = SongForm2
    success_url = reverse_lazy('music:songs_list')
    template_name_suffix = '_delete'
    template_name = 'music/song/song_delete.html'


class SongCreate(CreateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Song
    form_class = SongForm2
    template_name = 'music/song/song_create.html'

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
            song = form.save(commit=False)
            song.user = self.request.user
            #song.cover = request.FILES['cover']
            #file_type = song.cover.url.split('.')[-1]
            #file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
            #    context = {
            #        'song': song,
            #        'form': form,
            #        'error_message': 'Image file must be PNG, JPG, or JPEG',
            #    }
            #    return render(request, 'music/song_create.html', context)
            song.save()


def fav_song(request, song_id):
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
    song = get_object_or_404(Song, pk=song_id)
    if song.fav:
        song.fav = False
    else:
        song.fav = True
    song.save()
    album = song.album
    return render(request, 'music/album/album_detail.html', {'album': album})


def create_song(request, album_id):
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
    form = SongForm1(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    artist = album.artist
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.title == form.cleaned_data.get("title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/song/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.artist = artist
        song.save()
        return render(request, 'music/album/album_detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/song/create_song.html', context)