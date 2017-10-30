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
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from music.models import Genre, Song
from music.tables import GenreTable
from music.forms import GenreForm


class Genres(View):
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
                genre_ids = []
                genres = []
                for genre in Genre.objects.all():
                    genre_ids.append(genre.pk)
                    genres = Genre.objects.filter(pk__in=genre_ids)
                if filter_by == 'favorites':
                    genres = genres.filter(fav=True)
                paginate_genres = Paginator(genres, 20, body=3, margin=1, tail=1)
                try:
                    genres = paginate_genres.page(page)
                except PageNotAnInteger:
                    genres = paginate_genres.page(1)
                except EmptyPage:
                    genres = paginate_genres.page(paginate_genres.num_pages)
            except Genre.DoesNotExist:
                genres = []
            return render(request, 'music/genre/genres.html', {
                'genre_list': genres,
                'filter_by': filter_by,
            })


class GenreList(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/genre/genre_table.html'
    model = Genre

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
            context = super(GenreList, self).get_context_data(**kwargs)
            table = GenreTable(Genre.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


class GenreDetailView(DetailView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/genre/genre_detail.html'
    model = Genre

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
            genres = Genre.objects.all()
            genres = Genre.objects.all()
            songs = Song.objects.all()
            genre = self.object
            context = super(GenreDetailView, self).get_context_data(**kwargs)
            context['genre'] = genre
            context['user'] = user
            return context


class GenreUpdate(UpdateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Genre
    form_class = GenreForm
    template_name = 'music/genre/genre_update.html'

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
        genre = form.save(commit=False)
        genre.user = self.request.user
        genre.save()
        return super(GenreUpdate, self).form_valid(form)


class GenreView(FormView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/genre/genre_create.html'
    form_class = GenreForm
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
            genre = form.save(commit=False)
            genre.user = self.request.user
            genre.save()
            return super(GenreView, self).form_valid(form)


class GenreDelete(DeleteView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Genre
    success_url = reverse_lazy('music:genres_list')
    template_name_suffix = '_delete'
    template_name = 'music/genre/genre_delete.html'


class GenreCreate(CreateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Genre
    form_class = GenreForm
    template_name = 'music/genre/genre_create.html'

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
            genre = form.save(commit=False)
            genre.user = self.request.user
            #genre.cover = request.FILES['cover']
            #file_type = genre.cover.url.split('.')[-1]
            #file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
            #    context = {
            #        'genre': genre,
            #        'form': form,
            #        'error_message': 'Image file must be PNG, JPG, or JPEG',
            #    }
            #    return render(request, 'music/genre_create.html', context)
            genre.save()


def fav_genre(request, genre_id):
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
    genre = get_object_or_404(Genre, pk=genre_id)
    if genre.fav:
        genre.fav = False
    else:
        genre.fav = True
        genre.save()
    genres = Genre.objects.all()
    return render(request, 'music/label/labels.html', {'genre': genres})
