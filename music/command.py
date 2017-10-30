"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from elasticsearch.client import IndicesClient
from django.conf import settings
from elasticsearch.helpers import bulk
from django.core.management.base import BaseCommand
from music.models import *


class Command(BaseCommand):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """

    # todo Finish docstring

    def handle(self, *args, **options):
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

        self.recreate_index()
        self.push_db_to_index()

    def recreate_index(self, model):
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
        indices_client = IndicesClient(client=settings.ES_CLIENT)
        index_name = model._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=model._meta.es_type_name,
            body=model._meta.es_mapping,
            index=index_name
        )

    def push_db_to_index(self, model):
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
        data = [
            self.convert_for_bulk(s, 'create') for s in model.objects.all()
        ]
        bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, django_object, action=None):
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
        data = django_object.es_repr()
        metadata = {
            '_op_type': action,
            "_index": django_object._meta.es_index_name,
            "_type": django_object._meta.es_type_name,
        }
        data.update(**metadata)
        return data