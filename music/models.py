from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from .search import AlbumIndex
from django.contrib.auth.models import User
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping', 'es_client'
)
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.helpers import scan

ELASTIC_SEARCH_NODES = ['http://localhost:9200']
INDEX = 'audiad'
ES_CLIENT = Elasticsearch(ELASTIC_SEARCH_NODES, verify_certs=True, connection_class=RequestsHttpConnection)
# from django.db.models.signals musicimport post_save
# from django.dispatch musicimport receiver


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     tags = TaggableManager(blank=True)
#     genres = models.ManyToManyField(Genre, blank=True, default=None)
#     styles = models.ManyToManyField(Style, blank=True, default=None)
#     artists = models.ManyToManyField(Artist, blank=True, default=None)
#     songs = models.ManyToManyField(Song, blank=True, default=None)
#     labels = models.ManyToManyField(Label, blank=True, default=None)
#     albums = models.ManyToManyField(Album, blank=True, default=None)


#     def __str__(self):
#         return self.bio


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()

#
# class mp3tag(models.Model):
#     discnumber = models.CharField(max_length=50, blank=True)
#     totaldiscs = models.CharField(max_length=50, blank=True)
#     totaltracks = models.CharField(max_length=50, blank=True)
#     titlesortorder = models.CharField(max_length=50, blank=True)
#     album = models.CharField(max_length=50, blank=True)
#     albumsortorder = models.CharField(max_length=50, blank=True)
#     origalbum = models.CharField(max_length=50, blank=True)
#     subtitle = models.CharField(max_length=50, blank=True)
#     setsubtitle = models.CharField(max_length=50, blank=True)
#     artist = models.CharField(max_length=50, blank=True)
#     performersortorder = models.CharField("", max_length=50, blank=True)
#     wwwartist = models.CharField(max_length=50, blank=True)
#     origartist = models.CharField(max_length=50, blank=True)
#     band = models.CharField(max_length=50, blank=True)
#     composer = models.CharField(max_length=50, blank=True)
#     lyricist = models.CharField(max_length=50, blank=True)
#     origlyricist = models.CharField(max_length=50, blank=True)
#     conductor = models.CharField(max_length=50, blank=True)
#     mixartist = models.CharField(max_length=50, blank=True)
#     publisher = models.CharField(max_length=50, blank=True)
#     wwwpublisher = models.CharField(max_length=50, blank=True)
#     encodedby = models.CharField(max_length=50, blank=True)
#     involvedpeople = models.CharField(max_length=50, blank=True)
#     musiciancreditlist = models.CharField(max_length=50, blank=True)
#     genre = models.CharField(max_length=50, blank=True)
#     mood = models.CharField(max_length=50, blank=True)
#     mediatype = models.CharField(max_length=50, blank=True)
#     wwwaudiosource = models.CharField(max_length=50, blank=True)
#     language = models.CharField(max_length=50, blank=True)
#     contentgroup = models.CharField(max_length=50, blank=True)
#     recordingtime = models.CharField(max_length=50, blank=True)
#     releasetime = models.CharField(max_length=50, blank=True)
#     encodingtime = models.CharField(max_length=50, blank=True)
#     taggingtime = models.CharField(max_length=50, blank=True)
#     origreleasetime = models.CharField(max_length=50, blank=True)
#     comment = models.CharField(max_length=50, blank=True)
#     popularimeter = models.CharField(max_length=50, blank=True)
#     playcounter = models.CharField(max_length=50, blank=True)
#     encodersettings = models.CharField(max_length=50, blank=True)
#     songlen = models.CharField(max_length=50, blank=True)
#     filetype = models.CharField(max_length=50, blank=True)
#     seekframe = models.CharField(max_length=50, blank=True)
#     mpeglookup = models.CharField(max_length=50, blank=True)
#     audioseekpoint = models.CharField(max_length=50, blank=True)
#     playlistdelay = models.CharField(max_length=50, blank=True)
#     eventtiming = models.CharField(max_length=50, blank=True)
#     syncedtempo = models.CharField(max_length=50, blank=True)
#     positionsync = models.CharField(max_length=50, blank=True)
#     buffersize = models.CharField(max_length=50, blank=True)
#     bpm = models.CharField(max_length=50, blank=True)
#     initialkey = models.CharField(max_length=50, blank=True)
#     volumeadj = models.CharField(max_length=50, blank=True)
#     reverb = models.CharField(max_length=50, blank=True)
#     equalizations = models.CharField(max_length=50, blank=True)
#     isrc = models.CharField(max_length=50, blank=True)
#     cdid = models.CharField(max_length=50, blank=True)
#     uniquefileid = models.CharField(max_length=50, blank=True)
#     wwwcommercialinfo = models.CharField(max_length=50, blank=True)
#     wwwpayment = models.CharField(max_length=50, blank=True)
#     fileowner = models.CharField(max_length=50, blank=True)
#     commercial = models.CharField(max_length=50, blank=True)
#     copyright = models.CharField(max_length=50, blank=True)
#     producednotice = models.CharField(max_length=50, blank=True)
#     termsofuse = models.CharField(max_length=50, blank=True)
#     wwwcopyright = models.CharField(max_length=50, blank=True)
#     ownership = models.CharField(max_length=50, blank=True)
#     audiocrypto = models.CharField(max_length=50, blank=True)
#     cryptoreg = models.CharField(max_length=50, blank=True)
#     groupingreg = models.CharField(max_length=50, blank=True)
#     signature = models.CharField(max_length=50, blank=True)
#     unsyncedlyrics = models.CharField(max_length=50, blank=True)
#     syncedlyrics = models.CharField(max_length=50, blank=True)
#     picture = models.CharField(max_length=50, blank=True)
#     generalobject = models.CharField(max_length=50, blank=True)
#     private = models.CharField(max_length=50, blank=True)
#     usertext = models.CharField(max_length=50, blank=True)
#     linkedinfo = models.CharField(max_length=50, blank=True)
#     origfilename = models.CharField(max_length=50, blank=True)
#     netradiostation = models.CharField(max_length=50, blank=True)
#     netradioowner = models.CharField(max_length=50, blank=True)
#     wwwradiopage = models.CharField(max_length=50, blank=True)
#     wwwuser = models.CharField(max_length=50, blank=True)
#     wwwaudiofile = models.CharField(max_length=50, blank=True)
#
#     @property
#     def __str__(self):
#         return self.song


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    fav = models.BooleanField(default=False, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, default=None)

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

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Genre, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Genre, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Genre Name: {}".format(self.name)

    def __str__(self):
        return self.name

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    class Meta:
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Country, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Country, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Country Name: {}".format(self.name)

    def __str__(self):
        return self.name

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    tags = TaggableManager(blank=True)
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Style, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Style, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Style Name: {}".format(self.name)

    def __str__(self):
        return self.name

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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


class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False)
    realname = models.CharField(max_length=200, blank=True, null=True, default=None)
    profile = models.CharField(max_length=2000, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True, default=None)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
    genre = models.ManyToManyField(Genre, blank=True, default=None)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Artist, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Artist, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Artist Name: {}".format(self.name)

    def __str__(self):
        return self.name

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
    name = models.CharField(max_length=200, blank=True, default=None, null=True)
    discogs_url = models.URLField(max_length=200, blank=True, null=True)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Label, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Label, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Label Name: {}".format(self.name)

    def __str__(self):
        return self.name

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
    user = models.ForeignKey(User, default=1)
    profile = models.CharField(max_length=2000, blank=True, default="")
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, blank=True, default=None)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, blank=True, default="")
    style = models.ManyToManyField(Style, blank=True, default="")
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, blank=True, default="")
    title = models.CharField(max_length=500, blank=False)
    subtitle = models.CharField(max_length=500, blank=True)
    producer = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True, default=None)
    month = models.CharField(max_length=50, blank=True, default="")
    day = models.CharField(max_length=50, blank=True, default="")
    year = models.IntegerField(null=True, blank=True, default=None)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, default="")
    cover = models.FileField(null=True, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    tracks = models.CharField(max_length=50, blank=True, default="")
    albumtype = models.CharField(max_length=50, blank=True, default="")
    mediums = models.CharField(max_length=50, blank=True, default="")
    releasegroup_id = models.CharField(max_length=50, blank=True, default="")
    catalognum = models.CharField(max_length=50, blank=True, default="")
    data_source = models.CharField(max_length=50, blank=True, default="")
    data_url = models.URLField(max_length=200, blank=True)

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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.title)
        #
        is_new = self.pk
        super(Album, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Album, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Album Title: {}".format(self.title)

    def __str__(self):
        return self.title

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        if not self.style.exists():
            return []
        return [c.style.name for c in self.style.all()]


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, blank=True, on_delete=models.CASCADE)
    profile = models.CharField(max_length=2000, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True, null=True)
    style = models.ManyToManyField(Style, blank=True, default=None)
    track = models.IntegerField(null=True, blank=True, default=None)
    title = models.CharField(max_length=500, blank=False)
    fav = models.BooleanField(default=False, blank=True)
    length = models.TimeField(null=True, blank=True, default=None)
    audio_file = models.FileField(null=True, blank=True, default="")
    last_played = models.DateField(null=True, blank=True, default=None)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    index = models.CharField(max_length=50, blank=True, default="")
    disc_number = models.IntegerField(blank=True, default=1)
    data_source = models.CharField(max_length=50, blank=True, default="")
    data_url = models.URLField(max_length=200, blank=True, null=True)
    # producer = models.CharField(max_length=200, blank=True)
    # media = models.CharField(max_length=50, blank=True, default="")
    # medium = models.CharField(max_length=50, blank=True, default="")
    # medium_index = models.CharField(max_length=50, blank=True, default="")
    # medium_total = models.CharField(max_length=50, blank=True, default="")
    # artist_sort = models.CharField(max_length=50, blank=True, default="")
    # artist_credit = models.CharField(max_length=50, blank=True, default="")
    # lyricist = models.CharField(max_length=50, blank=True, default="")
    # composer = models.CharField(max_length=50, blank=True, default="")
    # composer_sort = models.CharField(max_length=50, blank=True, default="")
    # arranger = models.CharField(max_length=50, blank=True, default="")
    # track_alt = models.CharField(max_length=50, blank=True, default="")
    # mp3tag = models.OneToOneField(mp3tag, on_delete=models.CASCADE, blank=True)

    class Meta:
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
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)
        #
        is_new = self.pk
        super(Song, self).save(*args, **kwargs)

        payload = self.es_repr()
        if is_new is not None:
            del payload['_id']
            ES_CLIENT.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )
        else:
            ES_CLIENT.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body={
                    'doc': payload
                }
            )

    def delete(self, *args, **kwargs):
        prev_pk = self.pk
        super(Song, self).delete(*args, **kwargs)
        ES_CLIENT.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )

    def __unicode__(self):
        return "Song Title: {}".format(self.title)

    def __str__(self):
        return self.title

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data

    def field_es_repr(self, field_name):
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
        if not self.style.exists():
            return []
        return [c.style.name for c in self.style.all()]

    # def get_es_tags(self):
    #     if not self.tags.exists():
    #         return []
    #     return [c.tag for c in self.tags.all()]
