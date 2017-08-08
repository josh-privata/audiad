from digg_paginator import DiggPaginator as Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from music.forms import AlbumForm
from music.models import Album, Artist, Song


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


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    albums()


def fav_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if album.fav:
        album.fav = False
    else:
        album.fav = True
    album.save()
    albums = Album.objects.all()
    return render(request, 'music/album/albums.html', {'albums': albums})


def albums(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        page = request.GET.get('page', 1)
        try:
            album_ids = []
            user_albums = []
            for album in Album.objects.filter(user=request.user):
                album_ids.append(album.pk)
                user_albums = Album.objects.filter(pk__in=album_ids)
            if user_albums:
                if filter_by == 'favorites':
                    user_albums = user_albums.filter(fav=True)
            paginate_albums = Paginator(user_albums, 20, body=3, margin=1, tail=1)
            try:
                user_albums = paginate_albums.page(page)
            except PageNotAnInteger:
                user_albums = paginate_albums.page(1)
            except EmptyPage:
                user_albums = paginate_albums.page(paginate_albums.num_pages)
        except Album.DoesNotExist:
            user_albums = []
        return render(request, 'music/album/albums.html', {
            'albums': user_albums,
            'filter_by': filter_by,
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
        similar_album = albums.filter(Q(genre__name__icontains=genre)).distinct().exclude(title=album.title).filter(artist=F('artist')).distinct()[:5]
        similar_song = songss.filter(Q(genre__name__icontains=genre)).distinct().exclude(album=album.id)[:5]
        return render(request, 'music/album/album_detail.html', {'album': album,
                                                                 'user': user,
                                                                 'similar_artist': similar_artist,
                                                                 'similar_album': similar_album,
                                                                 'similar_song': similar_song})


def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album)
    if form.is_valid():
        album.save()
        return render(request, 'music/album/album_detail.html', {
                               'album': album})
    return render(request, 'music/album/album_edit.html', {'form': form,
                                                           'album': album})