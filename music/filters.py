"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

import django_filters
from .models import Album, Artist, Song, Genre, Label


class AlbumFilter(django_filters.FilterSet):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    title = django_filters.CharFilter(lookup_expr='icontains')
    artist = django_filters.CharFilter(name='artist__name', lookup_expr='icontains')
    genre = django_filters.CharFilter(name='genre__name', lookup_expr='icontains')
    profile = django_filters.CharFilter(lookup_expr='icontains')
    style = django_filters.CharFilter(name='style__name', lookup_expr='icontains')
    label = django_filters.CharFilter(name='label__name', lookup_expr='icontains')
    subtitle = django_filters.CharFilter(lookup_expr='icontains')
    producer = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.CharFilter(lookup_expr='icontains')
    month = django_filters.CharFilter(lookup_expr='icontains')
    day = django_filters.CharFilter(lookup_expr='icontains')
    discogs_url = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    tracks = django_filters.CharFilter(lookup_expr='icontains')
    albumtype = django_filters.CharFilter(lookup_expr='icontains')
    fav = django_filters.CharFilter(lookup_expr='icontains')
    mediums = django_filters.CharFilter(lookup_expr='icontains')
    releasegroup_id = django_filters.CharFilter(lookup_expr='icontains')
    catalognum = django_filters.CharFilter(lookup_expr='icontains')
    data_source = django_filters.CharFilter(lookup_expr='icontains')
    data_url = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        exclude = ['cover']


class ArtistFilter(django_filters.FilterSet):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    title = django_filters.CharFilter(lookup_expr='icontains')
    style = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.CharFilter(name='genre__name', lookup_expr='icontains')
    profile = django_filters.CharFilter(lookup_expr='icontains')
    discogs_url = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    length = django_filters.CharFilter(lookup_expr='icontains')
    audio_file = django_filters.CharFilter(lookup_expr='icontains')
    last_played = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Artist
        exclude = ['fav']


class SongFilter(django_filters.FilterSet):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = django_filters.CharFilter(lookup_expr='icontains')
    artist = django_filters.CharFilter(name='artist__name', lookup_expr='icontains')
    album = django_filters.CharFilter(name='album__title', lookup_expr='icontains')
    genre = django_filters.CharFilter(name='genre__name', lookup_expr='icontains')
    profile = django_filters.CharFilter(lookup_expr='icontains')
    discogs_url = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Song
        exclude = ['fav']


class GenreFilter(django_filters.FilterSet):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    parent = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Genre
        exclude = ['fav']


class LabelFilter(django_filters.FilterSet):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    profile = django_filters.CharFilter(lookup_expr='icontains')
    discogs_url = django_filters.CharFilter(lookup_expr='icontains')
    contact = django_filters.CharFilter(lookup_expr='icontains')
    parent = django_filters.CharFilter(lookup_expr='icontains')
    website = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Label
        exclude = ['fav', 'logo']
