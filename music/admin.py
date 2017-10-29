from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Album, Artist, Song, Genre, User, Label, Country, Style

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'User Profile'
#     fk_name = 'user'
#
#
# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name')
#     list_select_related = ('profile',)
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class ArtistAdmin(admin.ModelAdmin):
    list_filter = ['genre', 'fav', 'tags']
    search_fields = ['name', 'tags', 'genre']


class AlbumAdmin(admin.ModelAdmin):
    list_filter = ['genre', 'tags', 'fav']
    search_fields = ['artist', 'title', 'genre', 'label', 'subtitle', 'producer', 'date',
                     'year', 'cover', 'discogs_url', 'fav', 'tags']


class SongAdmin(admin.ModelAdmin):
    list_filter = ['genre', 'fav', 'tags']
    search_fields = ['genre', 'title', 'artist', 'album', 'track', 'fav', 'length',
                     'last_played', 'tags']


class GenreAdmin(admin.ModelAdmin):
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'fav', 'tags']


class CountryAdmin(admin.ModelAdmin):
    list_filter = ['tags']
    search_fields = ['name', 'tags']


class StyleAdmin(admin.ModelAdmin):
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'fav', 'tags']


class LabelAdmin(admin.ModelAdmin):
    list_filter = ['fav', 'tags']
    search_fields = ['name', 'discogs_url', 'fav', 'tags', 'profile', 'contact', 'parent', 'website', 'logo', 'slug']

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Genre, GenreAdmin)

