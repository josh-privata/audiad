"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from elasticsearch import Elasticsearch, RequestsHttpConnection
ES_CLIENT = Elasticsearch(
    ['http://127.0.0.1:9200/'],

)