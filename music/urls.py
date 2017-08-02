from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import views

app_name = 'music'
urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/albums/<all:favourites>
    url(r'^albums/(?P<filter_by>[a-zA_Z]+)/$', views.albums, name='albums'),

  # /music/songs/<all:favourites>
  url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # /music/songs/<all:favourites>
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/table$', views.songstable, name='songstable'),

    # /music/artists/<all:favourites>
    url(r'^artists/(?P<filter_by>[a-zA_Z]+)/$', views.artists, name='artists'),

    # /music/albums/<album_id>/detail/
    url(r'^albums/(?P<album_id>[0-9]+)/detail/$', views.album_detail, name='album_detail'),

    # /music/songs/<song id>/detail/
    url(r'^songs/(?P<song_id>[0-9]+)/detail/$', views.song_detail, name='song_detail'),

    # /music/<artist id>/detail/
    url(r'^artists/(?P<artist_id>[0-9]+)/detail/$', views.artist_detail, name='artist_detail'),

    # /music/albums/<album_id>/edit/
    url(r'^albums/(?P<album_id>[0-9]+)/edit/$', views.edit_album, name='edit_album'),

    # /music/songs/<song id>/edit/
    url(r'^songs/(?P<song_id>[0-9]+)/edit/$', views.edit_song, name='edit_song'),

    # /music/<artist id>/edit/
    url(r'^artists/(?P<artist_id>[0-9]+)/edit/$', views.edit_artist, name='edit_artist'),

    # /music/<song_id>/favorite_song
    url(r'^(?P<song_id>[0-9]+)/favorite_song/$', views.fav_song, name='fav_song'),

    # /music/<artist_id>/favorite_artist
    url(r'^(?P<artist_id>[0-9]+)/favorite_artist/$', views.fav_artist, name='fav_artist'),

    # /music/<album_id>/favorite_album
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.fav_album, name='fav_album'),

    # /music/create_album
    url(r'^create_album/$', views.create_album, name='create_album'),

    # /music/search_results
    url(r'^search_results/$', views.searchresults, name='searchresults'),

    # /music/create_artist
    url(r'^create_artist/$', views.create_artist, name='create_artist'),

    # /music/create_genre
    url(r'^create_genre/$', views.create_genre, name='create_genre'),

    # /music/<album_id>/create_song
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    # /music/<song_id>/delete_song
    url(r'^(?P<song_id>[0-9]+)/delete_song//$', views.delete_song, name='delete_song'),

    # /music/<album_id>/delete_album
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    # /music/<album_id>/delete_artist
    url(r'^(?P<album_id>[0-9]+)/delete_artist/$', views.delete_artist, name='delete_artist'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # url(r'^profile/$', views.update_profile, name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

