import django_tables2 as tables
from music.models import *


class SongTable(tables.Table):
    class Meta:
        model = Song
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('discogs_url', 'profile', 'id', 'length', 'audio_file', 'producer', 'last_played', 'slug')


class ArtistTable(tables.Table):
    class Meta:
        model = Artist
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('discogs_url', 'profile', 'id', 'length', 'audio_file', 'producer', 'last_played', 'slug')


class AlbumTable(tables.Table):
    class Meta:
        model = Album
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class GenreTable(tables.Table):
    class Meta:
        model = Genre
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class LabelTable(tables.Table):
    class Meta:
        model = Label
        attrs = {'class': 'table table-bordered table-striped table-hover'}


