"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django import forms
from django.contrib.auth.models import User
from .models import Album, Song, Artist, Genre, Label


class UserForm(forms.ModelForm):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('user', 'bio', 'tags')


class AlbumForm(forms.ModelForm):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """

    # todo Finish docstring
    class Meta:
        model = Album
        fields = ['artist', 'title', 'subtitle', 'tags']


class SongForm1(forms.ModelForm):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """

    # todo Finish docstring
    class Meta:
        model = Song
        fields = ['title', 'artist', 'tags']


class ArtistForm(forms.ModelForm):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    class Meta:
        model = Artist
        fields = ['name', 'discogs_url', 'fav', 'tags']


class GenreForm(forms.ModelForm):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """

    # todo Finish docstring
    class Meta:
        model = Genre
        fields = ['name', 'fav', 'tags']


class LabelForm(forms.ModelForm):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    class Meta:
        model = Label
        fields = ['name', 'fav', 'tags']


class SongForm2(forms.ModelForm):
    """docstring

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """

    # todo Finish docstring
    class Meta:
        model = Song
        fields = ('title', 'artist', 'album', 'track', 'fav', 'length',
                  'last_played', 'tags')


# class MP3Form(forms.ModelForm):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring
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
