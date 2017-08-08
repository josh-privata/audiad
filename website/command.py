from elasticsearch.client import IndicesClient
from django.conf import settings
from elasticsearch.helpers import bulk
from django.core.management.base import BaseCommand
from music.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.recreate_index()
        self.push_db_to_index()

    def recreate_index(self, model):
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

    def push_db_to_index(self, model):
        data = [
            self.convert_for_bulk(s, 'create') for s in Song.objects.all()
        ]
        bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, django_object, action=None):
        data = django_object.es_repr()
        metadata = {
            '_op_type': action,
            "_index": django_object._meta.es_index_name,
            "_type": django_object._meta.es_type_name,
        }
        data.update(**metadata)
        return data