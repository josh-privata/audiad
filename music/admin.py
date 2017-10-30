"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Album, Artist, Song, Genre, User, Label, Country, Style


class ArtistAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['genre', 'fav', 'tags']
    search_fields = ['name', 'tags', 'genre']


class AlbumAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['genre', 'tags', 'fav']
    search_fields = ['artist', 'title', 'genre', 'label', 'subtitle', 'producer', 'date',
                     'year', 'cover', 'discogs_url', 'fav', 'tags']


class SongAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['genre', 'fav', 'tags']
    search_fields = ['genre', 'title', 'artist', 'album', 'track', 'fav', 'length',
                     'last_played', 'tags']


class GenreAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'fav', 'tags']


class CountryAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['tags']
    search_fields = ['name', 'tags']


class StyleAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'fav', 'tags']


class LabelAdmin(admin.ModelAdmin):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'discogs_url', 'fav', 'tags', 'profile', 'contact', 'parent', 'website', 'logo', 'slug']

# class ProfileInline(admin.StackedInline):
# todo Finish docstring
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'User Profile'
#     fk_name = 'user'
#
#
# class CustomUserAdmin(UserAdmin):
# todo Finish docstring
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name')
#     list_select_related = ('profile',)
#
#   def get_inline_instances(self, request, obj=None):
# todo Finish docstring
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Genre, GenreAdmin)

