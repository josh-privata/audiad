from django import forms
from django.contrib.auth.models import User
from .models import Album, Song, Artist, Genre


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('user', 'bio', 'tags')


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'title', 'genre', 'subtitle', 'producer', 'date',
                  'year', 'cover', 'discogs_url', 'fav', 'tags']


class SongForm1(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'tags']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'discogs_url', 'fav', 'tags']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'fav', 'tags']


class SongForm2(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'album', 'track', 'fav', 'length',
                  'last_played', 'tags')


# class MP3Form(forms.ModelForm):
#     class Meta:
#         model = mp3tag
#         fields = ('tracknumber', 'discnumber', 'totaldiscs', 'totaltracks', 'title',
#                   'titlesortorder', 'album', 'albumsortorder', 'origalbum', 'subtitle', 'setsubtitle', 'artist',
#                   'performersortorder', 'wwwartist', 'origartist', 'band', 'composer', 'lyricist', 'origlyricist',
#                   'conductor', 'mixartist', 'publisher', 'encodedby', 'involvedpeople', 'musiciancreditlist',
#                   'genre', 'mood', 'mediatype', 'wwwaudiosource', 'language', 'contentgroup', 'recordingtime',
#                   'releasetime', 'encodingtime', 'taggingtime', 'origreleasetime', 'comment', 'popularimeter',
#                   'playcounter', 'encodersettings', 'songlen', 'filetype', 'seekframe', 'mpeglookup',
#                   'audioseekpoint', 'playlistdelay', 'eventtiming', 'syncedtempo', 'positionsync', 'buffersize', 'bpm',
#                   'initialkey', 'volumeadj', 'reverb', 'equalizations', 'isrc', 'cdid',
#                   'uniquefileid', 'wwwcommercialinfo', 'wwwpayment', 'commercial', 'copyright', 'producednotice',
#                   'termsofuse', 'wwwcopyright', 'ownership', 'audiocrypto', 'cryptoreg', 'groupingreg', 'signature',
#                   'unsyncedlyrics', 'syncedlyrics', 'picture', 'generalobject', 'private', 'usertext', 'linkedinfo',
#                   'origfilename', 'netradiostation', 'netradioowner', 'wwwradiopage', 'wwwuser', 'wwwaudiofile'
#                   )
