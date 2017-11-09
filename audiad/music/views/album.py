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
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView, View
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from audiad.music.forms import AlbumForm
from audiad.music.models import Album, Artist, Song
from audiad.music.tables import AlbumTable as AT
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class Albums(View):
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
                album_ids = []
                user_albums = []
                for album in Album.objects.filter(user=request.user):
                    album_ids.append(album.pk)
                    user_albums = Album.objects.filter(pk__in=album_ids)
                if user_albums:
                    if filter_by == 'favorites':
                        user_albums = user_albums.filter(fav=True)
                paginate_albums = Paginator(user_albums, 20, body=3, margin=1, tail=1)
                try:
                    user_albums = paginate_albums.page(page)
                except PageNotAnInteger:
                    user_albums = paginate_albums.page(1)
                except EmptyPage:
                    user_albums = paginate_albums.page(paginate_albums.num_pages)
            except Album.DoesNotExist:
                user_albums = []
            return render(request, 'music/album/albums.html', {
                'album_list': user_albums,
                'filter_by': filter_by,
            })


class AlbumTable(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/album/album_table.html'
    model = Album

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
            context = super(AlbumTable, self).get_context_data(**kwargs)
            table = AT(Album.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


class AlbumList(ListView):
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
                album_ids = []
                albums = []
                for album in Album.objects.all():
                    album_ids.append(album.pk)
                    albums = Album.objects.filter(pk__in=album_ids)
                if filter_by == 'favorites':
                    albums = albums.filter(fav=True)
                paginate_albums = Paginator(albums, 20, body=3, margin=1, tail=1)
                try:
                    albums = paginate_albums.page(page)
                except PageNotAnInteger:
                    albums = paginate_albums.page(1)
                except EmptyPage:
                    albums = paginate_albums.page(paginate_albums.num_pages)
            except Album.DoesNotExist:
                albums = []
            return render(request, 'music/album/album_list.html', {
                'album_list': albums,
                'filter_by': filter_by,
            })


class AlbumDetailView(DetailView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/album/album_detail.html'
    model = Album

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
            albums = Album.objects.all()
            artists = Artist.objects.all()
            songs = Song.objects.all()
            album = self.object
            context = super(AlbumDetailView, self).get_context_data(**kwargs)
            context['album'] = album
            context['user'] = user
            if self.object.genre.name:
                genre = self.object.genre.name
            context['similar_artist'] = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=album.artist)[:5]
            context['similar_album'] = albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(title=album.title).filter(artist=F('artist')).distinct()[:5]
            context['similar_song'] = songs.filter(Q(genre__name__icontains=genre)).distinct().exclude(album=album.id)[:5]
            return context


class AlbumUpdate(UpdateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    # todo Doesnt populate fields
    model = Album
    form_class = AlbumForm
    template_name = 'music/album/album_update.html'
    success_url = reverse_lazy('music:albums' 'all')

    def get_initial(self):
        initial = super(AlbumUpdate, self).get_initial()
        return initial


class AlbumView(FormView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/album/album_create.html'
    form_class = AlbumForm
    success_url = '/index/'

    # def form_valid(self, form):
    #     """docstring
    #
    #             Note:
    #                 Do not include the `self` parameter in the ``Args`` section.
    #
    #             Args:
    #                 param1: The first parameter.
    #                 param2: The second parameter.
    #
    #             Returns:
    #                 True if successful, False otherwise.
    #
    #             """
    #     # todo Finish docstring
    #     if not self.request.user.is_authenticated():
    #         return render(self.request, 'music/auth/login.html')
    #     else:
    #         album = form.save(commit=False)
    #         album.user = self.request.user
    #         album.save()
    #         return super(AlbumView, self).form_valid(form)


class AlbumDelete(DeleteView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Album
    success_url = reverse_lazy('music:albums_list')
    template_name_suffix = '_delete'
    template_name = 'music/album/album_delete.html'


class AlbumCreate(CreateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Album
    form_class = AlbumForm
    template_name = 'music/album/album_create.html'

    # def form_valid(self, form):
    #     """docstring
    #
    #             Note:
    #                 Do not include the `self` parameter in the ``Args`` section.
    #
    #             Args:
    #                 param1: The first parameter.
    #                 param2: The second parameter.
    #
    #             Returns:
    #                 True if successful, False otherwise.
    #
    #             """
    #     # todo Finish docstring
    #     if not self.request.user.is_authenticated():
    #         return render(self.request, 'music/auth/login.html')
    #     else:
    #         album = form.save(commit=False)
    #         album.user = self.request.user
    #         #album.cover = request.FILES['cover']
    #         #file_type = album.cover.url.split('.')[-1]
    #         #file_type = file_type.lower()
    #         #if file_type not in IMAGE_FILE_TYPES:
    #         #    context = {
    #         #        'album': album,
    #         #        'form': form,
    #         #        'error_message': 'Image file must be PNG, JPG, or JPEG',
    #         #    }
    #         #    return render(request, 'music/album_create.html', context)
    #         album.save()


def fav_album(request, album_id):
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
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.fav:
            album.fav = False
        else:
            album.fav = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})
