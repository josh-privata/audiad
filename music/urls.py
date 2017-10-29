from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import music.views.genre
from music.views.views import *
from music.views.album import *
from music.views.song import *
from music.views.artist import *
from music.views.label import *
from music.views.genre import *
from haystack.generic_views import SearchView

from music.views.views import IndexView, MySearchView
from .views import views, song, album, artist, label, genre

app_name = 'music'
urlpatterns = [

    # BASE PAGES ##
    # /music/
    url(r'^$', IndexView.as_view(), name='index'),

    # ALBUMS ##
    # /music/view/albums/<all:favourites>
    url(r'^view/albums/(?P<filter_by>[a-zA_Z]+)/$', Albums.as_view(), name='albums'),
    # /music/view/album/<album_id>
    url(r'^view/album/(?P<pk>\d+)/$', AlbumView.as_view(), name='album_form'),
    # /music/list/albums/<all:favourites>
    url(r'^list/albums/$', AlbumList.as_view(), name='albums_list'),
    # /music/detail/albums/<album_id>
    url(r'^detail/album/(?P<pk>\d+)$', AlbumDetailView.as_view(), name='album_detail'),
    # /music/edit/albums/<album_id>/
    url(r'^edit/album/(?P<pk>\d+)$', AlbumUpdate.as_view(), name='edit_album'),
    # /music/delete/albums/<album_id>
    url(r'^delete/album/(?P<pk>\d+)$', AlbumDelete.as_view(), name='delete_album'),
    # /music/create/album
    url(r'^create/album/$', AlbumCreate.as_view(), name='create_album'),
    # /music/favorite_album/<album_id>
    url(r'^favorite_album/(?P<album_id>[0-9]+)$', album.fav_album, name='fav_album'),
    # /music/filter/albums/
    url(r'^filter/albums$', views.filter_album, name='filter_album'),

    # SONGS ##
    # /music/songs/<all:favourites>
    url(r'^view/songs/(?P<filter_by>[a-zA_Z]+)/$', Songs.as_view(), name='songs'),
    # /music/songs/<all:favourites>
    url(r'^list/songs/$', SongList.as_view(), name='songs_list'),
    # /music/songs/<song_id>
    url(r'^detail/song/(?P<pk>\d+)$', SongDetailView.as_view(), name='song_detail'),
    # /music/songs/<song_id>/view
    url(r'^view/song/(?P<pk>\d+)/$', SongView.as_view(), name='song_form'),
    # /music/songs/<song_id>/edit/
    url(r'^edit/song/(?P<pk>\d+)$', SongUpdate.as_view(), name='edit_song'),
    # /music/songs/<song_id>/delete
    url(r'^delete/song/(?P<pk>\d+)$', SongDelete.as_view(), name='delete_song'),
    # /music/create/songs
    url(r'^create/song/$', SongCreate.as_view(), name='create_song'),
    # /music/<song_id>/favorite_song
    url(r'^(?P<song_id>[0-9]+)/favorite_song/$', song.fav_song, name='fav_song'),
    # /music/filter/songs/
    url(r'^filter/songs', views.filter_song, name='filter_songs'),

    # ARTISTS ##
    # /music/artist/<all:favourites>
    url(r'^view/artists/(?P<filter_by>[a-zA_Z]+)/$', Artists.as_view(), name='artists'),
    # /music/artist/<all:favourites>
    url(r'^list/artists/$', ArtistList.as_view(), name='artist_list'),
    # /music/artist/<artist_id>
    url(r'^detail/artist/(?P<pk>\d+)$', ArtistDetailView.as_view(), name='artist_detail'),
    # /music/artist/<artist_id>/view
    url(r'^view/artist/(?P<pk>\d+)/$', ArtistView.as_view(), name='artist_form'),
    # /music/artist/<artist_id>/edit/
    url(r'^edit/artist/(?P<pk>\d+)$', ArtistUpdate.as_view(), name='edit_artist'),
    # /music/artist/<artist_id>/delete
    url(r'^delete/artist/(?P<pk>\d+)$', ArtistDelete.as_view(), name='delete_artist'),
    # /music/create/artist
    url(r'^create/artist/$', ArtistCreate.as_view(), name='create_artist'),
    # /music/<artist_id>/favorite_artist
    url(r'^(?P<artist_id>[0-9]+)/favorite_artist/$', artist.fav_artist, name='fav_artist'),
    # /music/filter/artists/
    url(r'^filter/artists', views.filter_artist, name='filter_artist'),
    
    # GENRE ##
    # /music/genre/<all:favourites>
    url(r'^view/genres/(?P<filter_by>[a-zA_Z]+)/$', Genres.as_view(), name='genres'),
    # /music/genre/<all:favourites>
    url(r'^list/genres/$', GenreList.as_view(), name='genre_list'),
    # /music/genre/<genre_id>
    url(r'^detail/genre/(?P<pk>\d+)$', GenreDetailView.as_view(), name='genre_detail'),
    # /music/genre/<genre_id>/view
    url(r'^view/genre/(?P<pk>\d+)/$', GenreView.as_view(), name='genre_form'),
    # /music/genre/<genre_id>/edit/
    url(r'^edit/genre/(?P<pk>\d+)$', GenreUpdate.as_view(), name='edit_genre'),
    # /music/genre/<genre_id>/delete
    url(r'^delete/genre/(?P<pk>\d+)$', GenreDelete.as_view(), name='delete_genre'),
    # /music/create/genre
    url(r'^create/genre/$', GenreCreate.as_view(), name='create_genre'),
    # /music/<genre_id>/favorite_genre
    url(r'^(?P<genre_id>[0-9]+)/favorite_genre/$', genre.fav_genre, name='fav_genre'),

    # LABEL ##
    # /music/label/<all:favourites>
    url(r'^view/labels/(?P<filter_by>[a-zA_Z]+)/$', Labels.as_view(), name='labels'),
    # /music/label/<all:favourites>
    url(r'^list/labels/$', LabelList.as_view(), name='label_list'),
    # /music/label/<label_id>
    url(r'^detail/label/(?P<pk>\d+)$', LabelDetailView.as_view(), name='label_detail'),
    # /music/label/<label_id>/view
    url(r'^view/label/(?P<pk>\d+)/$', LabelView.as_view(), name='label_form'),
    # /music/label/<label_id>/edit/
    url(r'^edit/label/(?P<pk>\d+)$', LabelUpdate.as_view(), name='edit_label'),
    # /music/label/<label_id>/delete
    url(r'^delete/label/(?P<pk>\d+)$', LabelDelete.as_view(), name='delete_label'),
    # /music/create/label
    url(r'^create/label/$', LabelCreate.as_view(), name='create_label'),
    # /music/<label_id>/favorite_label
    url(r'^(?P<label_id>[0-9]+)/favorite_label/$', label.fav_label, name='fav_label'),

    # SEARCH ##
    # /music/search_results
    url(r'^search_results/$', views.searchresults, name='searchresults'),
    # /music/search
    url(r'^search/', MySearchView.as_view(), name='search'),

    # USER AND AUTH ##
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # url(r'^profile/$', views.update_profile, name='update_profile'),

    # MEDIA ##
    # url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, }),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
