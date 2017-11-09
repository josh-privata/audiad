"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django.db import models
from django.contrib.auth.models import User
import django.db.models.options as options
from django.template.defaultfilters import slugify
from django.urls import reverse
from elasticsearch import Elasticsearch, RequestsHttpConnection
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from mptt.models import MPTTModel, TreeForeignKey
# from django.db.models.signals musicimport post_save
# from django.dispatch musicimport receiver
# from elasticsearch.helpers import scan
# from taggit.managers import TaggableManager
from audiad.music.managers import SongManager

app_label = 'music'

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('es_index_name', 'es_type_name', 'es_mapping', 'es_client')
"""int: Module level variable documented inline."""
# todo Finish docstring

ELASTIC_SEARCH_NODES = ['http://localhost:9200']
"""int: Module level variable documented inline."""
# todo Finish docstring

INDEX = 'audiad'
"""int: Module level variable documented inline."""
# todo Finish docstring

ES_CLIENT = Elasticsearch(ELASTIC_SEARCH_NODES, verify_certs=True, connection_class=RequestsHttpConnection)
"""int: Module level variable documented inline."""
# todo Finish docstring


# Common Models
# todo uncomment URLS.PY
class Genre(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    #parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    #parent = models.ForeignKey('self', blank=True, null=True, default=None)
    tags = models.CharField(max_length=250, blank=True, null=True, default="genre")
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    fav = models.BooleanField(default=False, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        es_index_name = INDEX
        es_type_name = 'genre'
        es_mapping = {
            'properties': {
                'slug': {'type': 'string'},
                'name': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
                # 'parent': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short', "store": "yes"},
                #         'name': {'type': 'string'},
                #     }
                # },
            }
        }

    # Sample View
    # def show_genres(request):
    # return render_to_response("genres.html",
    #                       {'nodes':Genre.objects.all()},
    #                       context_instance=RequestContext(request))

    # Sample URL
    # (r'^genres/$', 'myapp.views.show_genres'),

    # Sample Template
    # {% load mptt_tags %}
    #     <ul>
    #         {% recursetree nodes %}
    #             <li>
    #                 {{ node.name }}
    #                 {% if not node.is_leaf_node %}
    #                     <ul class="children">
    #                         {{ children }}
    #                     </ul>
    #                 {% endif %}
    #             </li>
    #         {% endrecursetree %}
    #     </ul>


    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Genre, self).save(*args, **kwargs)

        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Genre, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def __unicode__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return "Genre Name: {}".format(self.name)

    def __str__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return self.name

    def es_repr(self):
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

        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value


class Country(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    tags = models.CharField(max_length=250, blank=True, null=True, default="country")
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    class Meta:
        app_label = 'music'
        es_index_name = INDEX
        es_type_name = 'country'
        es_mapping = {
            'properties': {
                'slug': {'type': 'string'},
                'name': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
            }
        }

    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Country, self).save(*args, **kwargs)
        #
        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Country, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def __unicode__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return "Country Name: {}".format(self.name)

    def __str__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return self.name

    def es_repr(self):
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
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value


class Style(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    tags = models.CharField(max_length=250, blank=True, null=True, default="style")
    fav = models.BooleanField(default=False, blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    class Meta:
        es_index_name = INDEX
        es_type_name = 'style'
        es_mapping = {
            'properties': {
                'slug': {'type': 'string'},
                'name': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
            }
        }

    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Style, self).save(*args, **kwargs)

        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Style, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def __unicode__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return "Style Name: {}".format(self.name)

    def __str__(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return self.name

    def es_repr(self):
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
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value


class Label(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = models.CharField(max_length=200, blank=True, default=None, null=True)
    discogs_url = models.URLField(max_length=200, blank=True, null=True)
    fav = models.BooleanField(default=False, blank=True)
    tags = models.CharField(max_length=250, blank=True, null=True, default="label")
    profile = models.CharField(max_length=2000, blank=True, default="", null=True)
    contact = models.CharField(max_length=200, blank=True, null=True, default=None)
    parent = models.CharField(max_length=200, blank=True, null=True, default=None)
    website = models.URLField(max_length=200, blank=True, null=True, default=None)
    logo = models.FileField(null=True, blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    class Meta:
        es_index_name = INDEX
        es_type_name = 'label'
        es_mapping = {
            'properties': {
                'fav': {'type': 'string'},
                'profile': {'type': 'date'},
                'contact': {'type': 'string'},
                'parent': {'type': 'integer'},
                'slug': {'type': 'string'},
                'website': {'type': 'string',
                            'index': "not_analyzed"},
                'discogs_url': {'type': 'string',
                                'index': "not_analyzed"},
                'name': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
                # 'data_url': {'type': 'string',
                #             'index': "not_analyzed"},
                # 'tags': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #     }
                # },
                # 'genre': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #         'name': {'type': 'string'},
                #     }
                # },
                # 'audio_file': {'type': 'string'},
                # 'title': {'type': 'string'},
            }
        }

    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Label, self).save(*args, **kwargs)
        #
        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Label, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def __unicode__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return "Label Name: {}".format(self.name)

    def __str__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return self.name

    def es_repr(self):
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
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value


# class Tag(models.Model):
#     name = models.CharField(max_length=250, blank=True, null=True, default="tag")
#     slug = models.CharField(max_length=250, blank=True, null=True, default=None)
#     fav = models.BooleanField(default=False, blank=True)
#
#     def save(self, *args, **kwargs):
#         # Create slug on object creation
#         if not self.id:
#             self.slug = slugify(self.name)
#         #
#         super(Tag, self).save(*args, **kwargs)


# Item Models
class Artist(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    name = models.CharField(max_length=200, blank=False)
    ''' Linked Fields '''
    style = models.ManyToManyField(Style, blank=True, default="")
    country = models.ForeignKey(Country, null=True, on_delete=models.DO_NOTHING, blank=True, default="")
    genre = models.ManyToManyField(Genre, blank=True, default=None)
    ''' Tag Specific Fields '''
    musicbrainz_artistid = models.CharField(max_length=500, blank=True, null=True, default=None)
    ''' Audiad Specific Fields '''
    # Artist real name (if using an alias etc Aphex Twin - > Richard James)
    realname = models.CharField(max_length=200, blank=True, null=True, default=None)
    # Discog.com URL
    discogs_url = models.URLField(max_length=200, null=True, blank=True, default="")
    # Custom URL
    website = models.CharField(max_length=250, null=True, blank=True, default="")
    # Custom Profile
    profile = models.TextField(max_length=2000, blank=True, default="")
    # User Favourite
    fav = models.BooleanField(default=False, blank=True)
    # Custom Tags todo implement taggit
    tags = models.CharField(max_length=250, blank=True, null=True, default="album")
    # Automated slug todo implement slug function in save()
    slug = models.SlugField(max_length=250, blank=True, null=True, default=None)
    # Add date
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    # Add date
    date_mod = models.DateTimeField(auto_now=True, null=True)
    # Custom Mood
    mood = models.CharField(max_length=250, null=True, blank=True, default="")

    class Meta:
        es_index_name = INDEX
        es_type_name = 'artist'
        es_mapping = {
            'properties': {
                'slug': {'type': 'string'},
                'realname': {'type': 'string'},
                'profile': {'type': 'string'},
                'discogs_url': {'type': 'string',
                                'index': "not_analyzed"},
                'website': {'type': 'string',
                            'index': "not_analyzed"},
                'name': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
                'country': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short', "store": "yes"},
                        'name': {'type': 'string'},
                    },
                },
                'fav': {'type': 'string'},
            }
        }

    def save(self, *args, **kwargs):
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
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Artist, self).save(*args, **kwargs)
        #
        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Artist, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def get_absolute_url(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return reverse('song_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return "Artist Name: {}".format(self.name)

    def __str__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return self.name

    def es_repr(self):
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

        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value


class Album(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    title = models.CharField(max_length=250, null=True, blank=True, default="")
    ''' Linked Fields '''
    user = models.ForeignKey(User, default=1)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, blank=True, default=None)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    style = models.ManyToManyField(Style, blank=True, default="")
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    ''' Tag Specific Fields '''
    albumartist = models.CharField(max_length=250, null=True, blank=True, default="")
    compilation = models.NullBooleanField(blank=True, default=False)
    catalognumber = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumtype = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumstatus = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumartistid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_artistid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_workid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_releasegroupid = models.CharField(max_length=250, null=True, blank=True, default="")
    language = models.CharField(max_length=250, null=True, blank=True, default="")
    albumartist_sort = models.CharField(max_length=250, null=True, blank=True, default="")
    albumartist_credit = models.CharField(max_length=250, null=True, blank=True, default="")
    year = models.IntegerField(null=True, blank=True, default=None)
    month = models.IntegerField(null=True, blank=True, default="")
    day = models.IntegerField(null=True, blank=True, default="")
    disctotal = models.IntegerField(null=True, blank=True, default="")
    albumtype = models.CharField(max_length=250, null=True, blank=True, default="")
    albumstatus = models.CharField(max_length=250, null=True, blank=True, default="")
    albumisambig = models.CharField(max_length=250, null=True, blank=True, default="")
    rg_album_gain = models.FloatField(max_length=30, null=True, blank=True, default="")
    rg_album_peak = models.FloatField(max_length=250, null=True, blank=True, default="")
    r128_album_gain = models.IntegerField(null=True, blank=True, default="")
    script = models.CharField(max_length=250, null=True, blank=True, default="")
    original_year = models.IntegerField(null=True, blank=True, default="")
    original_month = models.IntegerField(null=True, blank=True, default="")
    original_day = models.IntegerField(null=True, blank=True, default="")
    albumsort = models.CharField(max_length=250, null=True, blank=True, default="")
    media = models.CharField(max_length=250, null=True, blank=True, default="")
    asin = models.CharField(max_length=250, null=True, blank=True, default="")
    ''' Audiad Specific Fields '''
    # Discog.com URL
    discogs_url = models.URLField(max_length=200, null=True, blank=True, default="")
    # Custom URL
    website = models.CharField(max_length=250, null=True, blank=True, default="")
    # File URL
    data_url = models.URLField(max_length=200, blank=True, null=True)
    # Custom Profile
    profile = models.TextField(max_length=2000, blank=True, default="")
    # User Favourite
    fav = models.BooleanField(default=False, blank=True)
    # Custom Tags todo implement taggit
    tags = models.CharField(max_length=250, blank=True, null=True, default="album")
    # Automated slug todo implement slug function in save()
    slug = models.SlugField(max_length=250, blank=True, null=True, default=None)
    # Add date
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    # Add date
    date_mod = models.DateTimeField(auto_now=True, null=True)
    # Custom Mood
    mood = models.CharField(max_length=250, null=True, blank=True, default="")

    class Meta:
        es_index_name = INDEX
        es_type_name = 'album'
        es_mapping = {
            'properties': {
                'user': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short', "store": "yes"},
                        'username': {'type': 'string'},
                    },
                },
                'subtitle': {'type': 'string'},
                'producer': {'type': 'string'},
                'date': {'type': 'date'},
                'month': {'type': 'string'},
                'year': {'type': 'integer'},
                'day': {'type': 'string'},
                'country': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short', "store": "yes"},
                        'name': {'type': 'string'},
                    },
                },
                'profile': {'type': 'string'},
                'style': {'type': 'string'},
                'tracks': {'type': 'string'},
                'fav': {'type': 'string'},
                'mediums': {'type': 'string'},
                'catalognum': {'type': 'string'},
                'slug': {'type': 'string'},
                'albumtype': {'type': 'string'},
                'data_source': {'type': 'string'},
                'artist': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short'},
                        'name': {'type': 'string'},
                    }
                },
                'discogs_url': {'type': 'string',
                                'index': "not_analyzed"},
                'title': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
                # 'data_url': {'type': 'string',
                #             'index': "not_analyzed"},
                # 'tags': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #     }
                # },
                # 'genre': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #         'name': {'type': 'string'},
                #     }
                # },
                # 'audio_file': {'type': 'string'},
                # 'title': {'type': 'string'},
            }
        }

    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.title)
        #
        is_new = self.pk
        super(Album, self).save(*args, **kwargs)

        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Album, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def get_absolute_url(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return reverse('album_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return "Album Title: {}".format(self.title)

    def __str__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return self.title

    def es_repr(self):
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
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value

    def get_es_style(self):
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
        if not self.style.exists():
            return []
        return [c.style.name for c in self.style.all()]


class Song(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    title = models.CharField(max_length=250, null=True, blank=True, default="")
    ''' Linked Fields '''
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, blank=True, default="")
    style = models.ManyToManyField(Style, blank=True, default=None)
    ''' Tag Specific Fields '''
    author = models.CharField(max_length=250, null=True, blank=True, default="")
    albumartist = models.CharField(max_length=250, null=True, blank=True, default="")
    compilation = models.NullBooleanField(blank=True, default=False)
    conductor = models.CharField(max_length=250, null=True, blank=True, default="")
    catalognumber = models.CharField(max_length=250, null=True, blank=True, default="")
    musicip_puid = models.CharField(max_length=250, null=True, blank=True, default="")
    organization = models.CharField(max_length=250, null=True, blank=True, default="")
    composersort = models.CharField(max_length=250, null=True, blank=True, default="")
    artistsort = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_discid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumtype = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumstatus = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumartistid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_trmid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_trackid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_releasetrackid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_artistid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_albumid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_workid = models.CharField(max_length=250, null=True, blank=True, default="")
    musicbrainz_releasegroupid = models.CharField(max_length=250, null=True, blank=True, default="")
    bpm = models.IntegerField(null=True, blank=True, default="")
    titlesort = models.CharField(max_length=250, null=True, blank=True, default="")
    acoustid_id = models.CharField(max_length=250, null=True, blank=True, default="")
    language = models.CharField(max_length=250, null=True, blank=True, default="")
    encodedby = models.CharField(max_length=250, null=True, blank=True, default="")
    barcode = models.CharField(max_length=250, null=True, blank=True, default="")
    composer = models.CharField(max_length=250, null=True, blank=True, default="")
    albumartist_sort = models.CharField(max_length=250, null=True, blank=True, default="")
    albumartist_credit = models.CharField(max_length=250, null=True, blank=True, default="")
    length = models.CharField(max_length=250, null=True, blank=True, default="")
    performer = models.CharField(max_length=250, null=True, blank=True, default="")
    musicip_fingerprint = models.CharField(max_length=250, null=True, blank=True, default="")
    arranger = models.CharField(max_length=250, null=True, blank=True, default="")
    website = models.CharField(max_length=250, null=True, blank=True, default="")
    version = models.CharField(max_length=250, null=True, blank=True, default="")
    isrc = models.CharField(max_length=250, null=True, blank=True, default="")
    disctitle = models.CharField(max_length=250, null=True, blank=True, default="")
    discnumber = models.IntegerField(null=True, blank=True, default="")
    lyricist = models.CharField(max_length=250, null=True, blank=True, default="")
    acoustid_fingerprint = models.CharField(max_length=250, null=True, blank=True, default="")
    tracknumber = models.IntegerField(null=True, blank=True, default="")
    original_year = models.IntegerField(null=True, blank=True, default="")
    original_month = models.IntegerField(null=True, blank=True, default="")
    original_day = models.IntegerField(null=True, blank=True, default="")
    year = models.IntegerField(null=True, blank=True, default="")
    month = models.IntegerField(null=True, blank=True, default="")
    day = models.IntegerField(null=True, blank=True, default="")
    format = models.CharField(max_length=250, null=True, blank=True, default="")
    asin = models.CharField(max_length=250, null=True, blank=True, default="")
    channels = models.IntegerField(null=True, blank=True, default="")
    bitrate = models.CharField(max_length=250, null=True, blank=True, default="")
    samplerate = models.CharField(max_length=250, null=True, blank=True, default="")
    bitdepth = models.IntegerField(null=True, blank=True, default="")
    rg_track_gain = models.FloatField(max_length=25, null=True, blank=True, default="")
    rg_track_peak = models.FloatField(max_length=25, null=True, blank=True, default="")
    rg_album_gain = models.FloatField(max_length=25, null=True, blank=True, default="")
    rg_album_peak = models.FloatField(max_length=25, null=True, blank=True, default="")
    r128_album_gain = models.IntegerField(null=True, blank=True, default="")
    r128_track_gain = models.IntegerField(null=True, blank=True, default="")
    tracktotal = models.IntegerField(null=True, blank=True, default="")
    comments = models.CharField(max_length=250, null=True, blank=True, default="")
    ''' Audiad Specific Fields '''
    # Discog.com URL
    discogs_url = models.URLField(max_length=200, null=True, blank=True, default="")
    # Custom URL
    website = models.CharField(max_length=250, null=True, blank=True, default="")
    # File URL
    data_url = models.URLField(max_length=200, blank=True)
    # Custom Profile
    profile = models.TextField(max_length=2000, blank=True, default="")
    # User Favourite
    fav = models.BooleanField(default=False, blank=True)
    # Custom Tags todo implement taggit
    tags = models.CharField(max_length=250, blank=True, null=True, default="album")
    # Automated slug todo implement slug function in save()
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    # Filepath
    file_path = models.CharField(max_length=255, blank=True, default="")
    # Add date
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    # Add date
    date_mod = models.DateTimeField(auto_now=True, null=True)
    # Custom Mood
    mood = models.CharField(max_length=250, null=True, blank=True, default="")


    objects = SongManager()

    class Meta:

        # Elastic Search Details
        es_index_name = INDEX
        es_type_name = 'song'
        es_mapping = {
            'properties': {
                'album': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short', "store": "yes"},
                        'title': {'type': 'string'},
                        'catalognum': {'type': 'string'},
                        'slug': {'type': 'string'},
                        'albumtype': {'type': 'string'},
                        'data_source': {'type': 'string'},
                        'subtitle': {'type': 'string'},
                        'producer': {'type': 'string'},
                        'date': {'type': 'date'},
                    }
                },
                'artist': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'short'},
                        'realname': {'type': 'string'},
                        'profile': {'type': 'string'},
                        'discogs_url': {'type': 'string',
                                        'index': "not_analyzed"},
                        'website': {'type': 'string',
                                    'index': "not_analyzed"},
                        'name': {
                            'type': 'completion',
                            'analyzer': 'simple',
                            'preserve_separators': True,
                            'preserve_position_increments': True,
                            'max_input_length': 200,
                        },
                    }
                },
                'profile': {'type': 'string'},
                'discogs_url': {'type': 'string',
                                'index': "not_analyzed"},
                'style': {'type': 'string'},
                'track': {'type': 'string'},
                'fav': {'type': 'string'},
                'length': {'type': 'string'},
                'last_played': {'type': 'string'},
                'slug': {'type': 'string'},
                'index': {'type': 'string'},
                'data_source': {'type': 'string'},
                'data_url': {'type': 'string',
                             'index': "not_analyzed"},
                'title': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 200,
                },
                # 'tags': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #     }
                # },
                # 'genre': {
                #     'type': 'object',
                #     'properties': {
                #         'id': {'type': 'short'},
                #         'name': {'type': 'string'},
                #     }
                # },
                # 'audio_file': {'type': 'string'},
                # 'title': {'type': 'string'},
            }
        }

    def save(self, *args, **kwargs):
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Song, self).save(*args, **kwargs)

        # payload = self.es_repr()
        # if is_new is not None:
        #     del payload['_id']
        #     ES_CLIENT.update(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )
        # else:
        #     ES_CLIENT.create(
        #         index=self._meta.es_index_name,
        #         doc_type=self._meta.es_type_name,
        #         id=self.pk,
        #         refresh=True,
        #         body={
        #             'doc': payload
        #         }
        #     )

    def delete(self, *args, **kwargs):
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
        prev_pk = self.pk
        super(Song, self).delete(*args, **kwargs)
        # ES_CLIENT.delete(
        #     index=self._meta.es_index_name,
        #     doc_type=self._meta.es_type_name,
        #     id=prev_pk,
        #     refresh=True,
        # )

    def get_absolute_url(self):
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring
        return reverse('song_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return "Item Title: {}".format(self.title)

    def __str__(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring

        return self.title

    def es_repr(self):
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
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        config = self._meta.es_mapping['properties'][field_name]
        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {'_id': related_object.pk}
                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)
        return field_es_value

    def get_es_style(self):
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
        if not self.style.exists():
            return []
        return [c.style.name for c in self.style.all()]

    # def get_es_tags(self):
    #     if not self.tags.exists():
    #         return []
    #     return [c.tag for c in self.tags.all()]


class Art(models.Model):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.
    """
    # todo Finish docstring
    pic_OTHER = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_FILE_ICON = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_OTHER_FILE_ICON = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_COVER_FRONT = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_COVER_BACK = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_LEAFLET_PAGE = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_MEDIA = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_LEAD_ARTIST = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_ARTIST = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_CONDUCTOR = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_BAND = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_COMPOSER = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_LYRICIST = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_RECORDING_LOCATION = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_DURING_RECORDING = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_DURING_PERFORMANCE = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_SCREEN_CAPTURE = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_FISH = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_ILLUSTRATION = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_BAND_LOGOTYPE = models.CharField(max_length=250, null=True, blank=True, default="")
    pic_PUBLISHER_LOGOTYPE = models.CharField(max_length=250, null=True, blank=True, default="")

    @property
    def __str__(self):
        return self.song


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True, default="")
#     tags = TaggableManager(blank=True)
# #    genres = models.ManyToManyField(Genre, blank=True, default=None)
# #    styles = models.ManyToManyField(Style, blank=True, default=None)
# #    artists = models.ManyToManyField(Artist, blank=True, default=None)
# #    songs = models.ManyToManyField(Item, blank=True, default=None)
# #    labels = models.ManyToManyField(Label, blank=True, default=None)
# #    albums = models.ManyToManyField(Album, blank=True, default=None)
#
#     def __str__(self):
#         return self.bio
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             UserProfile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.UserProfile.save()


