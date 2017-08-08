from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from music.forms import ArtistForm
from music.models import Album, Artist, Song


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


def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    artist()


def fav_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if artist.fav:
        artist.fav = False
    else:
        artist.fav = True
        artist.save()
    artists = Artist.objects.all()
    return render(request, 'music/artist/artists.html', {'artists': artists})


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