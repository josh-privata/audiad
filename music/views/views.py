from apt.progress.text import _
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.db.models import Q
from django_tables2 import RequestConfig

from music.forms import AlbumForm, ArtistForm, GenreForm, SongForm2, SongForm1, UserForm
from music.models import Album, Song, Artist
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from music.tables import *
from music.bin import *
from django.shortcuts import get_object_or_404, render, redirect

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            #album.cover = request.FILES['cover']
            #file_type = album.cover.url.split('.')[-1]
            #file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
            #    context = {
            #        'album': album,
            #        'form': form,
            #        'error_message': 'Image file must be PNG, JPG, or JPEG',
            #    }
            #    return render(request, 'music/create_album.html', context)
            album.save()
            return render(request, 'music/album/album_detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'music/album/create_album.html', context)


def create_artist(request):
    form = ArtistForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artist = form.save(commit=False)
        artist.save()
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums})
    context = {
        "form": form,
    }
    return render(request, 'music/artist/create_artist.html', context)


def create_genre(request):
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        genre = form.save(commit=False)
        genre.save()
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums})
    context = {
        "form": form,
    }
    return render(request, 'music/genre/create_genre.html', context)


def create_song(request, album_id):
    form = SongForm1(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    artist = album.artist
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.title == form.cleaned_data.get("title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/song/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.artist = artist
        song.save()
        return render(request, 'music/album/album_detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/song/create_song.html', context)


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    albums()


def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    artist()


def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()
    songs()


def fav_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if song.fav:
        song.fav = False
    else:
        song.fav = True
    song.save()
    album = song.album
    return render(request, 'music/album/album_detail.html', {'album': album})


def fav_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if album.fav:
        album.fav = False
    else:
        album.fav = True
    album.save()
    albums = Album.objects.all()
    return render(request, 'music/album/albums.html', {'albums': albums})


def fav_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if artist.fav:
        artist.fav = False
    else:
        artist.fav = True
        artist.save()
    artists = Artist.objects.all()
    return render(request, 'music/artist/artists.html', {'artists': artists})


def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            user_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                user_songs = user_songs.filter(fav=True)
        except Album.DoesNotExist:
            user_songs = []
        return render(request, 'music/song/songs.html', {
        'song_list': user_songs,
        'filter_by': filter_by,
    })


def songstable(request, filter_by):
    table = SongTable(Song.objects.all())
    if filter_by == 'favorites':
        table = table.filter(fav=True)
    RequestConfig(request).configure(table)
    return render(request, 'music/song/songs2.html', {'table': table})



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        user_songs = Song.objects.filter(fav=True)
        user_artists = Artist.objects.filter(fav=True)
        user_albums = Album.objects.filter(user=request.user, fav=True)
        albums_count = Album.objects.filter(user=request.user).count()
        artists_count = Artist.objects.all().count()
        songs_count = Song.objects.all().count()
        return render(request, 'music/index.html', {'artists_count': artists_count,
                                                    'user_albums': user_albums,
                                                    'user_songs': user_songs,
                                                    "user_artists": user_artists,
                                                    'songs_count': songs_count,
                                                    'albums_count': albums_count})


def albums(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        try:
            album_ids = []
            user_albums = []
            for album in Album.objects.filter(user=request.user):
                album_ids.append(album.pk)
                user_albums = Album.objects.filter(pk__in=album_ids)
            if user_albums:
                if filter_by == 'favorites':
                    user_albums = user_albums.filter(fav=True)
        except Album.DoesNotExist:
            user_albums = []
        return render(request, 'music/album/albums.html', {
            'albums': user_albums,
            'filter_by': filter_by,
        })


def artists(request, filter_by):
    try:
        artist_ids = []
        artists = []
        for artist in Artist.objects.all():
            artist_ids.append(artist.pk)
            artists = Artist.objects.filter(pk__in=artist_ids)
        if filter_by == 'favorites':
            artists = artists.filter(fav=True)
    except Artist.DoesNotExist:
        artists = []
    return render(request, 'music/artist/artists.html', {
        'artists': artists,
        'filter_by': filter_by,
    })


def searchresults(request):
    albums = Album.objects.all()
    artists = Artist.objects.all()
    songss = Song.objects.all()
    query = request.GET.get("q")
    albums = albums.filter(Q(title__icontains=query))
    songss = songss.filter(Q(title__icontains=query))
    artists = artists.filter(Q(name__icontains=query))
    return render(request, 'music/search/searchresults.html', {
        'artists': artists,
        'albums': albums,
        'songs': songss,
    })


def album_detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        albums = Album.objects.all()
        artists = Artist.objects.all()
        songss = Song.objects.all()
        genre = ""
        if album.genre.name:
            genre = album.genre.name
        similar_artist = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=album.artist)[:5]
        similar_album = albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(title=album.title)[:5]
        similar_song = songss.filter(Q(genre__name__icontains=genre)).distinct().exclude(album=album.id)[:5]
        return render(request, 'music/album/album_detail.html', {'album': album,
                                                                 'user': user,
                                                                 'similar_artist': similar_artist,
                                                                 'similar_album': similar_album,
                                                                 'similar_song': similar_song})


def artist_detail(request, artist_id):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        user = request.user
        artist = get_object_or_404(Artist, pk=artist_id)
        albums = Album.objects.all()
        artists = Artist.objects.all()
        songss = Song.objects.all()
        genre = ""
        if artist.genre.name:
            genre = artist.genre.name
        similar_artist = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=artist.name)[:5]
        similar_album = albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(artist=artist.id)[:5]
        similar_song = songss.filter(Q(genre__name__icontains=genre)).distinct().exclude(artist=artist.id).distinct()[:5]
        return render(request, 'music/artist/artist_detail.html', {'artist': artist,
                                                                   'user': user,
                                                                   'similar_artist': similar_artist,
                                                                   'similar_album': similar_album,
                                                                   'similar_song': similar_song})


def song_detail(request, song_id):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        user = request.user
        song = Song.objects.get(pk=song_id)
        album = song.album
        all_albums = Album.objects.all()
        artists = Artist.objects.all()
        songss = Song.objects.all()
        genre = ""
        if song.genre.name:
            genre = song.genre.name
        similar_artist = artists.filter(Q(genre__name__icontains=genre)).distinct().exclude(name=album.artist)[:5]
        similar_album = all_albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(title=album.title)[:5]
        similar_song = songss.filter(Q(genre__name__icontains=genre)).distinct().exclude(album=album.id)[:5]
        return render(request, 'music/song/song_detail.html', {'song': song,
                                                               'user': user,
                                                               'album': album,
                                                               'similar_artist': similar_artist,
                                                               'similar_album': similar_album,
                                                               'similar_song': similar_song})


def edit_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    form = SongForm1(instance=song)
    if form.is_valid():
        song.save()
        all_songs = Song.objects.all()
        return render(request, 'music/song/songs.html', {
                               'song_list': all_songs,
                               'filter_by': all})
    return render(request, 'music/song/song_edit.html', {'form': form,
                                                         'song': song})


def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album)
    if form.is_valid():
        album.save()
        return render(request, 'music/album/album_detail.html', {
                               'album': album})
    return render(request, 'music/album/album_edit.html', {'form': form,
                                                           'album': album})


def edit_artist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    #form = ArtistForm(request.POST or None, request.FILES or None, instance=artist)
    form = ArtistForm(instance=artist)
    if form.is_valid():
        artist.save()
        all_songs = Song.objects.all()
        return render(request, 'music/song/songs.html', {
                              'song_list': all_songs,
                              'filter_by': all})
    return render(request, 'music/artist/artist_edit.html', {'form': form,
                                                             'artist': artist})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/auth/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/auth/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/auth/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/auth/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/auth/register.html', context)

#
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
