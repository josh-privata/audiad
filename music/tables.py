import django_tables2 as tables
from music.models import *

class SongTable(tables.Table):
    class Meta:
        model = Song
        attrs = {'class': 'paleblue'}