"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

import django_tables2 as tables
from music.models import *


class SongTable(tables.Table):
    # todo Finish docstring
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    class Meta:
        model = Song
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('discogs_url', 'profile', 'id', 'length', 'audio_file', 'producer', 'last_played', 'slug')


class ArtistTable(tables.Table):
    # todo Finish docstring
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    class Meta:
        model = Artist
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('discogs_url', 'profile', 'id', 'length', 'audio_file', 'producer', 'last_played', 'slug')


class AlbumTable(tables.Table):
    # todo Finish docstring
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    class Meta:
        model = Album
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class GenreTable(tables.Table):
    # todo Finish docstring
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    class Meta:
        model = Genre
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class LabelTable(tables.Table):
    # todo Finish docstring
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    class Meta:
        model = Label
        attrs = {'class': 'table table-bordered table-striped table-hover'}