from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import views, song, album, artist

app_name = 'music'
urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/albums/<all:favourites>
    url(r'^albums/(?P<filter_by>[a-zA_Z]+)/$', album.albums, name='albums'),

    # /music/songs/<all:favourites>
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', song.songs, name='songs'),

    # /music/songs/<all:favourites>
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/table$', song.songstable, name='songstable'),

    # /music/artists/<all:favourites>
    url(r'^artists/(?P<filter_by>[a-zA_Z]+)/$', artist.artists, name='artists'),

    # /music/albums/<album_id>/detail/
    url(r'^albums/(?P<album_id>[0-9]+)/detail/$', album.album_detail, name='album_detail'),

    # /music/songs/<song id>/detail/
    url(r'^songs/(?P<song_id>[0-9]+)/detail/$', song.song_detail, name='song_detail'),

    # /music/<artist id>/detail/
    url(r'^artists/(?P<artist_id>[0-9]+)/detail/$', artist.artist_detail, name='artist_detail'),

    # /music/albums/<album_id>/edit/
    url(r'^albums/(?P<album_id>[0-9]+)/edit/$', album.edit_album, name='edit_album'),

    # /music/songs/<song id>/edit/
    url(r'^songs/(?P<song_id>[0-9]+)/edit/$', song.edit_song, name='edit_song'),

    # /music/<artist id>/edit/
    url(r'^artists/(?P<artist_id>[0-9]+)/edit/$', artist.edit_artist, name='edit_artist'),

    # /music/<song_id>/favorite_song
    url(r'^(?P<song_id>[0-9]+)/favorite_song/$', song.fav_song, name='fav_song'),

    # /music/<artist_id>/favorite_artist
    url(r'^(?P<artist_id>[0-9]+)/favorite_artist/$', artist.fav_artist, name='fav_artist'),

    # /music/<album_id>/favorite_album
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', album.fav_album, name='fav_album'),

    # /music/create_album
    url(r'^create_album/$', album.create_album, name='create_album'),

    # /music/search_results
    url(r'^search_results/$', views.searchresults, name='searchresults'),

    # /music/create_artist
    url(r'^create_artist/$', artist.create_artist, name='create_artist'),

    # /music/create_genre
    url(r'^create_genre/$', views.create_genre, name='create_genre'),

    # /music/<album_id>/create_song
    url(r'^(?P<album_id>[0-9]+)/create_song/$', song.create_song, name='create_song'),

    # /music/<song_id>/delete_song
    url(r'^(?P<song_id>[0-9]+)/delete_song//$', song.delete_song, name='delete_song'),

    # /music/<album_id>/delete_album
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', album.delete_album, name='delete_album'),

    # /music/<album_id>/delete_artist
    url(r'^(?P<album_id>[0-9]+)/delete_artist/$', artist.delete_artist, name='delete_artist'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # url(r'^profile/$', views.update_profile, name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # coding: utf-8
# from django.conf musicimport settings
# from django.conf.urls musicimport include, url
# from django.contrib musicimport admin
# from django.views musicimport static
#
# from app.views musicimport ClassBased, FilteredPersonListView, MultipleTables, bootstrap, index, multiple, semantic, tutorial
#
# admin.autodiscover()
#
# urlpatterns = [
#     url(r'^$', index),
#     url(r'^multiple/', multiple, name='multiple'),
#     url(r'^class-based/$', ClassBased.as_view(), name='singletableview'),
#     url(r'^class-based-multiple/$', MultipleTables.as_view(), name='multitableview'),
#     url(r'^class-based-filtered/$', FilteredPersonListView.as_view(), name='filtertableview'),
#
#     url(r'^tutorial/$', tutorial, name='tutorial'),
#     url(r'^bootstrap/$', bootstrap, name='bootstrap'),
#     url(r'^semantic/$', semantic, name='semantic'),
#
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#     url(r'^admin/', include(admin.site.urls)),
#
#     url(r'^media/(?P<path>.*)$', static.serve, {
#         'document_root': settings.MEDIA_ROOT,
#     }),
# ]

