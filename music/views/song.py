from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from music.forms import SongForm1
from music.models import Album, Song, Artist
from music.tables import SongTable


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
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))
    return render(request, 'music/song/songs2.html', {'table': table})


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