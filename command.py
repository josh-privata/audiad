from elasticsearch.client import IndicesClient
from django.conf import settings
from elasticsearch.helpers import bulk
from django.core.management.base import BaseCommand
from music.models import *


class Command(BaseCommand):
    ES_CLIENT = Elasticsearch(
        ['http://127.0.0.1:9200/'], connection_class=RequestsHttpConnection)

    def handle(self, *args, **options):
        self.recreate_index()
        self.push_db_to_index()

    def recreate_index(self):
        indices_client = IndicesClient(client=settings.ES_CLIENT)
        index_name = Song._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Song._meta.es_type_name,
            body=Song._meta.es_mapping,
            index=index_name
        )
        index_name = Album._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Album._meta.es_type_name,
            body=Album._meta.es_mapping,
            index=index_name
        )
        index_name = Genre._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Genre._meta.es_type_name,
            body=Genre._meta.es_mapping,
            index=index_name
        )
        index_name = Artist._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Artist._meta.es_type_name,
            body=Artist._meta.es_mapping,
            index=index_name
        )
        index_name = Country._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Country._meta.es_type_name,
            body=Country._meta.es_mapping,
            index=index_name
        )
        index_name = Label._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Label._meta.es_type_name,
            body=Label._meta.es_mapping,
            index=index_name
        )
        index_name = Style._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Style._meta.es_type_name,
            body=Style._meta.es_mapping,
            index=index_name
        )

    def push_db_to_index(self):
        data = [
            self.convert_for_bulk(s, 'create') for s in Song.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Album.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Label.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Genre.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Artist.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Country.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)
        data = [
            self.convert_for_bulk(s, 'create') for s in Style.objects.all()
        ]
        bulk(client=ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, django_object, action=None):
        data = django_object.es_repr()
        metadata = {
            '_op_type': action,
            "_index": django_object._meta.es_index_name,
            "_type": django_object._meta.es_type_name,
        }
        data.update(**metadata)
        return data