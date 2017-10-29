import os

from datetime import date
import time

from music.models import Artist, Album, Song
from importer.musicimport import db_connect, mediafile

MEDIA_FORMATS = {
    'mp3':  'MP3',
    'aac':  'AAC',
    'alac': 'ALAC',
    'ogg':  'OGG',
    'opus': 'Opus',
    'flac': 'FLAC',
    'ape':  'APE',
    'wv':   'WavPack',
    'mpc':  'Musepack',
    'asf':  'Windows Media',
    'aiff': 'AIFF',
    'dsf':  'DSD Stream File',
}


# allocate path -> scan path for files -> determine audio formats -> yield: path, media file
#   -> create song object with file -> read metadata -> check for existing entry -> save data



class Directory:

    def __init__(self, path):
        self.path = path
        self._root = path

    @property
    def root(self):
        return self._root

    def sorted_walk(self, path, ignore=(), ignore_hidden=False, logger=None):
        """Like `os.walk`, but yields things in case-insensitive sorted,
        breadth-first order.  Directory and file names matching any glob
        pattern in `ignore` are skipped. If `logger` is provided, then
        warning messages are logged there when a directory cannot be listed.
        """
        # Make sure the pathes aren't Unicode strings.
        path = bytestring_path(path)
        ignore = [bytestring_path(i) for i in ignore]

        # Get all the directories and files at this level.
        try:
            contents = os.listdir(syspath(path))
        except OSError as exc:
            if logger:
                logger.warning(u'could not list directory {0}: {1}'.format(
                    displayable_path(path), exc.strerror
                ))
            return
        dirs = []
        files = []
        for base in contents:
            base = bytestring_path(base)

            # Skip ignored filenames.
            skip = False
            for pat in ignore:
                if fnmatch.fnmatch(base, pat):
                    skip = True
                    break
            if skip:
                continue

            # Add to output as either a file or a directory.
            cur = os.path.join(path, base)
            if (ignore_hidden and not hidden.is_hidden(cur)) or not ignore_hidden:
                if os.path.isdir(syspath(cur)):
                    dirs.append(base)
                else:
                    files.append(base)

        # Sort lists (case-insensitive) and yield the current level.
        dirs.sort(key=bytes.lower)
        files.sort(key=bytes.lower)
        yield (path, dirs, files)

        # Recurse into directories.
        for base in dirs:
            cur = os.path.join(path, base)
            # yield from sorted_walk(...)
            for res in sorted_walk(cur, ignore, ignore_hidden, logger):
                yield res

    def paths(self):
        """Walk `self.path` and yield `(dirs, files)` pairs where
        `files` are individual music files and `dirs` the set of
        containing directories where the music was found.

        This can either be a recursive search in the ordinary case, a
        single track when `path` is a file, a single directory in
        `flat` mode.
        """
        if not os.path.isdir(self.path):
            yield [self.path], [self.path]
        elif self.session.config['flat']:
            paths = []
            for dirs, paths_in_dir in self.files_in_path(self.path):
                paths += paths_in_dir
            yield [self.toppath], paths
        else:
            for dirs, paths in self.files_in_path(self.path):
                yield dirs, paths

    def files_in_path(path):
        for root, dirs, fs in sorted_walk(path):
            items = [os.path.join(root, f) for f in fs]
            if items:
                yield [root], items

    def get_directories(self):
        """
            Generator function
            :return: Yields a directory
         """
        yield [directory for directory in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, directory))]

    def get_files(self):
        """
        Generator function
        :return: Yields a file
        """
        yield [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]

    def check_format(self, file):
        for key in MEDIA_FORMATS.keys():
            if str(file).endswith(key):
                return True

class Item:
    """
    Base class for all songs
    """
    def __init__(self, file):
        self.path = file
        self.item = mediafile.MediaFile(self.path)
            
    def item(self):
        return self.item

    def path(self):
        return self.path

    def check_artist(self):
        ''' Get artist name '''
        artist = self.item.artist
        existing = Artist.objects.get(name=artist)
        try:
            ''' Lookup artist in db '''
            if existing.id is int:
                return True
            else:
                return False
        except:
            return False

    def check_album(self):
        ''' Get album name '''
        album = self.item.album
        artist = self.item.artist
        try:
            ''' Lookup artist in db '''
            temp = Album.objects.get(name=album)
            if temp.title == album and temp.artist.name == artist:
                return True
            else:
                return False
        except:
            return False

    def check_song(self):
        ''' Get label name  '''
        song = self.item.title
        artist = self.item.artist
        try:
            ''' Lookup artist in db '''
            temp = Item.objects.get(name='title')
            if temp.title == song and temp.artist.name == artist:
                return True
            else:
                return False
        except:
            return False

    def create_album(self):
        album = Album.objects.create()
        album.albumartist = self.item.albumartist
        album.albumartist_sort = self.item.albumartist_sort
        album.albumartist_credit = self.item.albumartist_credit
        album.album = self.item.album
        album.genre = self.item.genre
        album.year = self.item.year
        album.month = self.item.month
        album.day = self.item.day
        album.disctotal = self.item.disctotal
        album.comp = self.item.comp
        album.mb_albumid = self.item.mb_albumid
        album.mb_albumartistid = self.item.mb_albumartistid
        album.albumtype = self.item.albumtype
        album.label = self.item.label
        album.mb_releasegroupid = self.item.mb_releasegroupid
        album.asin = self.item.asin
        album.catalognum = self.item.catalognum
        album.script = self.item.script
        album.language = self.item.language
        album.country = self.item.country
        album.albumstatus = self.item.albumstatus
        album.albumdisambig = self.item.albumdisambig
        album.rg_album_gain = self.item.rg_album_gain
        album.rg_album_peak = self.item.rg_album_peak
        album.r128_album_gain = self.item.r128_album_gain
        album.original_year = self.item.original_year
        album.original_month = self.item.original_month
        album.original_day = self.item.original_day
        album.save()

    def create_song(self):
        song = Song.objects.create()
        song.path = self.item.path
        song.title = self.item.title
        song.artist = self.item.artist
        song.artist_sort = self.item.artist_sort
        song.artist_credit = self.item.artist_credit
        song.album = self.item.album
        song.albumartist = self.item.albumartist
        song.albumartist_sort = self.item.albumartist_sort
        song.albumartist_credit = self.item.albumartist_credit
        song.genre = self.item.genre
        song.lyricist = self.item.lyricist
        song.composer = self.item.composer
        song.composer_sort = self.item.composer_sort
        song.arranger = self.item.arranger
        song.grouping = self.item.grouping
        song.year = self.item.year
        song.month = self.item.month
        song.day = self.item.day
        song.track = self.item.track
        song.tracktotal = self.item.tracktotal
        song.disc = self.item.disc
        song.disctotal = self.item.disctotal
        song.lyrics = self.item.lyrics
        song.comments = self.item.comments
        song.bpm = self.item.bpm
        song.comp = self.item.comp
        song.mb_trackid = self.item.mb_trackid
        song.mb_albumid = self.item.mb_albumid
        song.mb_artistid = self.item.mb_artistid
        song.mb_albumartistid = self.item.mb_albumartistid
        song.albumtype = self.item.albumtype
        song.label = self.item.label
        song.acoustid_fingerprint = self.item.acoustid_fingerprint
        song.acoustid_id = self.item.acoustid_id
        song.mb_releasegroupid = self.item.mb_releasegroupid
        song.asin = self.item.asin
        song.catalognum = self.item.catalognum
        song.script = self.item.script
        song.language = self.item.language
        song.country = self.item.country
        song.albumstatus = self.item.albumstatus
        song.media = self.item.media
        song.albumdisambig = self.item.albumdisambig
        song.disctitle = self.item.disctitle
        song.encoder = self.item.encoder
        song.rg_track_gain = self.item.rg_track_gain
        song.rg_track_peak = self.item.rg_track_peak
        song.rg_album_gain = self.item.rg_album_gain
        song.rg_album_peak = self.item.rg_album_peak
        song.r128_track_gain = self.item.r128_track_gain
        song.r128_album_gain = self.item.r128_album_gain
        song.original_year = self.item.original_year
        song.original_month = self.item.original_month
        song.original_day = self.item.original_day
        song.initial_key = self.item.initial_key
        song.length = self.item.length
        song.bitrate = self.item.bitrate
        song.format = self.item.format
        song.samplerate = self.item.samplerate
        song.bitdepth = self.item.bitdepth
        song.channels = self.item.channels
        song.mtime = time.localtime(os.path.getmtime(self.path))
        song.save()

    def create_artist(self):
        artist = Artist.objects.create()
        artist.name = self.item.artist
        artist.realname = self.item.artist
        artist.profile = "profile"
        artist.discogs_url = "https://www.google.com"
        artist.website = "https://www.google.com"
        artist.fav = False
        artist.tags = self.item.album
        artist.genre = self.item.genre
        artist.country = self.item.country
        artist.musicbrainzid = self.item.mb_artistid
        artist.save()