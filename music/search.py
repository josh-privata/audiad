

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, Index
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import *
client = Elasticsearch()
my_search = Search(using=client)
connections.create_connection()


class AlbumIndex(DocType):

    class Meta:
        fields = ['title', 'artist']


album = Index('album')

album.settings(
    number_of_shards=1,
    number_of_replicas=0
)


def bulk_indexing():
    AlbumIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in Album.objects.all().iterator().__iter__()))


def search(title):
    query = my_search.query("match", title=title)
    response = query.execute()
    return response
