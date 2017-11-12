import os
import sys

from datetime import date
from mediafile import MediaFile
import sqlite3
import time

# from datetime import date
# from music.models import Artist, Album, Song
# from importer.musicimport import db_connect, mediafile

# MEDIA_FORMATS = {
#     'mp3':  'MP3',
#     'aac':  'AAC',
#     'alac': 'ALAC',
#     'ogg':  'OGG',
#     'opus': 'Opus',
#     'flac': 'FLAC',
#     'ape':  'APE',
#     'wv':   'WavPack',
#     'mpc':  'Musepack',
#     'asf':  'Windows Media',
#     'aiff': 'AIFF',
#     'dsf':  'DSD Stream File',
# }


DATABASE = "/home/josh/Code/Django/Projects/Audiad/audiad/mydatabase"

MEDIA_FORMATS = ('mp3', 'aac', 'alac', 'ogg', 'opus', 'flac', 'ape', 'wv', 'mpc', 'asf', 'aiff', 'dsf')

REMOVE = {'(', ')'}

USER = 1
# todo use mutagen to detect file type to avoid mpeg header error on wrongly named files

# DB Formatting
def replace(any_dict):
    for k, v in any_dict.items():
        if v is None:
            any_dict[k] = "Unknown"
        elif type(v) == type(any_dict):
            replace(v)


def slugify(string):
    if string:
        return ''.join('_' if c == ' ' else c for c in string if c not in REMOVE)
    else:
        pass


def raw_seconds_short(string):
    """Formats a human-readable M:SS string as a float (number of seconds).

    Raises ValueError if the conversion cannot take place due to `string` not
    being in the right format.
    """
    match = re.match(r'^(\d+):([0-5]\d)$', string)
    if not match:
        raise ValueError(u'String not in M:SS format')
    minutes, seconds = map(int, match.groups())
    return float(minutes * 60 + seconds)


def str2bool(value):
    """Returns a boolean reflecting a human-entered string."""
    return value.lower() in (u'yes', u'1', u'true', u't', u'y')


def as_string(value):
    """Convert a value to a Unicode object for matching with a query.
    None becomes the empty string. Bytestrings are silently decoded.
    """

    buffer_types = memoryview

    if value is None:
        return u''
    elif isinstance(value, buffer_types):
        return bytes(value).decode('utf-8', 'ignore')
    elif isinstance(value, bytes):
        return value.decode('utf-8', 'ignore')



def text_string(value, encoding='utf-8'):
    """Convert a string, which can either be bytes or unicode, to
    unicode.

    Text (unicode) is left untouched; bytes are decoded. This is useful
    to convert from a "native string" (bytes on Python 2, str on Python
    3) to a consistently unicode value.
    """
    if isinstance(value, bytes):
        return value.decode(encoding)
    return value


# Human output formatting.
def human_bytes(size):
    """Formats size, a number of bytes, in a human-readable way."""
    powers = [u'', u'K', u'M', u'G', u'T', u'P', u'E', u'Z', u'Y', u'H']
    unit = 'B'
    for power in powers:
        if size < 1024:
            return u"%3.1f %s%s" % (size, power, unit)
        size /= 1024.0
        unit = u'iB'
    return u"big"


def human_seconds(interval):
    """Formats interval, a number of seconds, as a human-readable time
    interval using English words.
    """
    units = [
        (1, u'second'),
        (60, u'minute'),
        (60, u'hour'),
        (24, u'day'),
        (7, u'week'),
        (52, u'year'),
        (10, u'decade'),
    ]
    for i in range(len(units) - 1):
        increment, suffix = units[i]
        next_increment, _ = units[i + 1]
        interval /= float(increment)
        if interval < next_increment:
            break
    else:
        # Last unit.
        increment, suffix = units[-1]
        interval /= float(increment)

    return u"%3.1f %ss" % (interval, suffix)


def human_seconds_short(interval):
    """Formats a number of seconds as a short human-readable M:SS
    string.
    """
    interval = int(interval)
    return u'%i:%02i' % (interval // 60, interval % 60)


class Item:
    """
    Base class for all songs
    """

    # todo Finish docstrings
    def __init__(self, file):
        self.path = file
        self.item = MediaFile(self.path)

    def item(self):
        return self.item

    def path(self):
        return self.path

    def genre(self):
        if self.item.genre is not None:
            return self.item.genre
        else:
            return "<unknown>"

    def country(self):
        if self.item.country:
            return self.item.country
        else:
            return "<unknown>"

    def style(self):
        if self.item.genre:
            return self.item.genre
        else:
            return "<unknown>"

    def song(self):
        if self.item.title:
            return self.item.title
        else:
            return "<unknown>"

    def artist(self):
        if self.item.artist:
            return self.item.artist
        else:
            return "<unknown>"

    def album(self):
        if self.item.album:
            return self.item.album
        else:
            return "<unknown>"

    def label(self):
        if self.item.label is not None:
            return self.item.label
        else:
            return "<unknown>"

    def get_song(self):
        return {'path': self.item.path,
                'title': self.item.title,
                'artist': self.item.artist,
                'artist_sort': self.item.artist_sort,
                'artist_credit': self.item.artist_credit,
                'album': self.item.album,
                'albumartist': self.item.albumartist,
                'albumartist_sort': self.item.albumartist_sort,
                'albumartist_credit': self.item.albumartist_credit,
                'genre': self.item.genre,
                'lyricist': self.item.lyricist,
                'composer': self.item.composer,
                'composer_sort': self.item.composer_sort,
                'arranger': self.item.arranger,
                'grouping': self.item.grouping,
                'year': self.item.year,
                'month': self.item.month,
                'day': self.item.day,
                'track': self.item.track,
                'tracktotal': self.item.tracktotal,
                'disc': self.item.disc,
                'disctotal': self.item.disctotal,
                'lyrics': self.item.lyrics,
                'comments': self.item.comments,
                'bpm': self.item.bpm,
                'comp': self.item.comp,
                'mb_trackid': self.item.mb_trackid,
                'mb_albumid': self.item.mb_albumid,
                'mb_artistid': self.item.mb_artistid,
                'mb_albumartistid': self.item.mb_albumartistid,
                'albumtype': self.item.albumtype,
                'label': self.item.label,
                'acoustid_fingerprint': self.item.acoustid_fingerprint,
                'acoustid_id': self.item.acoustid_id,
                'mb_releasegroupid': self.item.mb_releasegroupid,
                'asin': self.item.asin,
                'catalognum': self.item.catalognum,
                'script': self.item.script,
                'language': self.item.language,
                'country': self.item.country,
                'albumstatus': self.item.albumstatus,
                'media': self.item.media,
                'albumdisambig': self.item.albumdisambig,
                'disctitle': self.item.disctitle,
                'encoder': self.item.encoder,
                'rg_track_gain': self.item.rg_track_gain,
                'rg_track_peak': self.item.rg_track_peak,
                'rg_album_gain': self.item.rg_album_gain,
                'rg_album_peak': self.item.rg_album_peak,
                'r128_track_gain': self.item.r128_track_gain,
                'r128_album_gain': self.item.r128_album_gain,
                'original_year': self.item.original_year,
                'original_month': self.item.original_month,
                'original_day': self.item.original_day,
                'initial_key': self.item.initial_key,
                'length': self.item.length,
                'bitrate': self.item.bitrate,
                'format': self.item.format,
                'samplerate': self.item.samplerate,
                'bitdepth': self.item.bitdepth,
                'channels': self.item.channels,
                'mtime': time.localtime(os.path.getmtime(self.path))}

    def get_artist(self):
        return {'artist': self.item.artist,
                'realname': self.item.artist,
                'profile': "profile",
                'discogs_url': "https://www.google.com",
                'website': "https://www.google.com",
                'fav': False,
                'tags': self.item.album,
                'genre': self.item.genre,
                'country': self.item.country,
                'musicbrainzid': self.item.mb_artistid}

    def get_album(self):
        return {'albumartist': self.item.albumartist,
                'albumartist_sort': self.item.albumartist_sort,
                'albumartist_credit': self.item.albumartist_credit,
                'album': self.item.album,
                'genre': self.item.genre,
                'year': self.item.year,
                'month': self.item.month,
                'day': self.item.day,
                'disctotal': self.item.disctotal,
                'comp': self.item.comp,
                'mb_albumid': self.item.mb_albumid,
                'mb_albumartistid': self.item.mb_albumartistid,
                'albumtype': self.item.albumtype,
                'label': self.item.label,
                'mb_releasegroupid': self.item.mb_releasegroupid,
                'asin': self.item.asin,
                'catalognum': self.item.catalognum,
                'script': self.item.script,
                'language': self.item.language,
                'country': self.item.country,
                'albumstatus': self.item.albumstatus,
                'albumdisambig': self.item.albumdisambig,
                'rg_album_gain': self.item.rg_album_gain,
                'rg_album_peak': self.item.rg_album_peak,
                'r128_album_gain': self.item.r128_album_gain,
                'original_year': self.item.original_year,
                'original_month': self.item.original_month,
                'original_day': self.item.original_day}


# Required
# 1. Add a country(ies)
# 2. Add a label(s)
# 3. Add a genre(s)

# Next
# 4. Add an artist with a (genre, label, country)
# 5. Add an album with a (genre, label, country, artist)
# 6. Add a song with a (genre, label, country, artist, album)
def get_db(database):
    con = sqlite3.connect(database)
    with con:
        return con


def db_save(con):
    con.commit()


def db_close(con):
    con.close()


def delete_all(con):
    curs = con.cursor()
    curs.execute("""DELETE FROM music_album_genre""")
    curs.execute("""DELETE FROM music_genre""")
    curs.execute("""DELETE FROM music_album""")
    curs.execute("""DELETE FROM music_artist""")


def add_label(con, name=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    curs.execute("""INSERT INTO music_label(name, discogs_url, fav, profile, parent, website, logo, slug) 
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                 (name,
                  kwargs.get('discogs_url', ''),
                  kwargs.get('fav', '0'),
                  kwargs.get('profile', '<Unknown'),
                  kwargs.get('parent', '1'),
                  kwargs.get('website', 'http://google.com'),
                  kwargs.get('logo', ''),
                  slugify(name)))


def add_country(con, name=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    curs.execute("""INSERT INTO music_country(name, slug, tags) 
                 VALUES(?, ?, ?)""",
                 (name,
                  slugify(kwargs.get('slug', '')),
                  kwargs.get('logo', '')))


def add_style(con, name=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    curs.execute("""INSERT INTO music_style(name, tags, fav, slug)
                 VALUES(?, ?, ?, ?)""",
                 (name,
                  kwargs.get('tags', ''),
                  kwargs.get('fav', '0'),
                  slugify(name)))


def add_genre(con, name=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    curs.execute("""INSERT INTO music_genre(name, fav, tags, slug)
                 VALUES(?, ?, ?, ?)""",
                 (name,
                  kwargs.get('fav', '0'),
                  kwargs.get('tags', ''),
                  slugify(name)))


def add_artist(con, genres=None, countrys=None, artist=None, styles=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    country_id = curs.execute("""SELECT id FROM music_country WHERE music_country.name = ?""", (countrys,)).fetchone()
    genre_id = curs.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genres,)).fetchone()
    style_id = curs.execute("""SELECT id FROM music_style WHERE music_style.name = ?""", (styles,)).fetchone()
    print(genres, genre_id)
    print(countrys, country_id)
    print(styles, style_id)
    curs.execute("""INSERT INTO music_artist
                 (name, country_id, realname,
                  musicbrainz_artistid,
                  discogs_url,
                  profile,
                  fav,
                  tags,
                  slug,
                  website,
                  mood)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                 (artist, int(country_id[0]), artist,
                  kwargs.get('mb_artistid', ''),
                  # Audiad Specific Fields
                  kwargs.get('discogs_url', ''),
                  kwargs.get('profile', ''),
                  kwargs.get('fav', '0'),
                  kwargs.get('tags', ''),
                  slugify(artist),
                  kwargs.get('website', ''),
                  ''))
    db_save(con)
    artist_id = curs.lastrowid
    ''' Insert table dependencies '''
    curs.execute("""INSERT INTO music_artist_genre(artist_id, genre_id) VALUES(?,?)""",
                 (int(artist_id), int(genre_id[0])))
    print(artist_id)
    print(style_id)
    curs.execute("""INSERT INTO music_artist_style(artist_id, style_id) VALUES(?,?)""",
                 (int(artist_id), int(style_id[0])))


def add_album(con, countrys=None, genres=None, labels=None, artist=None, album=None, styles=None, **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    genre_id = curs.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genres,)).fetchone()
    artist_id = curs.execute("""SELECT id FROM music_artist WHERE music_artist.name = ?""", (artist,)).fetchone()
    label_id = curs.execute("""SELECT id FROM music_label WHERE music_label.name = ?""", (labels,)).fetchone()
    country_id = curs.execute("""SELECT id FROM music_country WHERE music_country.name = ?""", (countrys,)).fetchone()
    style_id = curs.execute("""SELECT id FROM music_style WHERE music_style.name = ?""", (styles,)).fetchone()
    print(genres, genre_id)
    print(artist, artist_id)
    print(labels, label_id)
    print(styles, style_id)
    print(countrys, country_id)
    print(album)
    curs.execute\
     ("""INSERT INTO music_album(title, genre_id, artist_id, user_id, label_id, country_id,
    albumartist,
    compilation,
    catalognumber,
    musicbrainz_albumtype,
    musicbrainz_albumstatus,
    musicbrainz_albumartistid,
    musicbrainz_artistid,
    musicbrainz_albumid,
    musicbrainz_workid,
    musicbrainz_releasegroupid,
    language,
    albumartist_sort,
    albumartist_credit,
    year,
    month,
    day,
    disctotal,
    albumtype,
    albumstatus,
    albumisambig,
    rg_album_gain,
    rg_album_peak,
    r128_album_gain,
    script,
    original_year,
    original_month,
    original_day,
    albumsort,
    media,
    asin,
    discogs_url,
    profile,
    fav,
    tags,
    slug,
    data_url,
    website,
    mood)
     VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
      ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
     (album, int(genre_id[0]), int(artist_id[0]), int(USER), int(label_id[0]), int(country_id[0]),
      kwargs.get('albumartist', ''),
      kwargs.get('compilation', ''),
      kwargs.get('catalognumber', ''),
      kwargs.get('musicbrainz_albumtype', ''),
      kwargs.get('musicbrainz_albumstatus', ''),
      kwargs.get('musicbrainz_albumartistid', ''),
      kwargs.get('musicbrainz_artistid', ''),
      kwargs.get('musicbrainz_albumid', ''),
      kwargs.get('musicbrainz_workid', ''),
      kwargs.get('musicbrainz_releasegroupid', ''),
      kwargs.get('language', ''),
      kwargs.get('albumartist_sort', ''),
      kwargs.get('albumartist_credit', ''),
      kwargs.get('year', ''),
      kwargs.get('month', ''),
      kwargs.get('day', ''),
      kwargs.get('disctotal', ''),
      kwargs.get('albumtype', ''),
      kwargs.get('albumstatus', ''),
      kwargs.get('albumisambig', ''),
      kwargs.get('rg_album_gain', ''),
      kwargs.get('rg_album_peak', ''),
      kwargs.get('r128_album_gain', ''),
      kwargs.get('script', ''),
      kwargs.get('original_year', ''),
      kwargs.get('original_month', ''),
      kwargs.get('original_day', ''),
      kwargs.get('albumsort', ''),
      kwargs.get('media', ''),
      kwargs.get('asin', ''),
      # Audiad Specific Fields
      kwargs.get('discogs_url', ''),
      kwargs.get('profile', ''),
      kwargs.get('fav', '0'),
      kwargs.get('tags', ''),
      slugify(album),
      kwargs.get('data_url', ''),
      kwargs.get('website', ''),
      kwargs.get('genre', '')))
    db_save(con)
    album_id = curs.lastrowid
    print(album_id)
    ''' Insert table dependencies '''
    curs.execute("""INSERT INTO music_album_style(album_id, style_id) VALUES(?,?)""",
                 (int(album_id), int(style_id[0])))


def add_song(con, filepath, genres=None, labels=None, countrys=None, artist=None, album=None, song=None, styles=None,  **kwargs):
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    genre_id = curs.execute("""SELECT id FROM music_genre WHERE music_genre.name  = ?""", (genres,)).fetchone()
    artist_id = curs.execute("""SELECT id FROM music_artist WHERE music_artist.name  = ?""", (artist,)).fetchone()
    album_id = curs.execute("""SELECT id FROM music_album WHERE music_album.title = ?""", (album,)).fetchone()
    label_id = curs.execute("""SELECT id FROM music_label WHERE music_label.name = ?""", (labels,)).fetchone()
    country_id = curs.execute("""SELECT id FROM music_country WHERE music_country.name = ?""", (countrys,)).fetchone()
    style_id = curs.execute("""SELECT id FROM music_style WHERE music_style.name = ?""", (styles,)).fetchone()
    curs.execute\
    ("""INSERT INTO music_song(title, album_id, genre_id, artist_id, label_id, country_id,
    author,
    albumartist,
    compilation,
    conductor,
    catalognumber,
    musicip_puid,
    organization,
    composersort,
    artistsort,
    musicbrainz_discid,
    musicbrainz_albumtype,
    musicbrainz_albumstatus,
    musicbrainz_albumartistid,
    musicbrainz_trmid,
    musicbrainz_trackid,
    musicbrainz_releasetrackid,
    musicbrainz_artistid,
    musicbrainz_albumid,
    musicbrainz_workid,
    musicbrainz_releasegroupid,
    bpm,
    titlesort,
    acoustid_id,
    language,
    encodedby,
    barcode,
    composer,
    albumartist_sort,
    albumartist_credit,
    length,
    performer,
    musicip_fingerprint,
    arranger,
    website,
    version,
    isrc,
    disctitle,
    discnumber,
    lyricist,
    acoustid_fingerprint,
    tracknumber,
    original_year,
    original_month,
    original_day,
    format,
    asin,
    channels,
    bitrate,
    samplerate,
    bitdepth,
    rg_track_gain,
    rg_track_peak,
    rg_album_gain,
    rg_album_peak,
    r128_album_gain,
    r128_track_gain,
    tracktotal,
    length,
    comments,
    discnumber,
    year,
    month,
    day,
    discogs_url,
    profile,
    fav,
    tags,
    slug,
    file_path,
    data_url,
    mood)
     VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?)""",
     (song, int(album_id[0]), int(genre_id[0]), int(artist_id[0]), int(label_id[0]), int(country_id[0]),
      kwargs.get('author', ''),
      kwargs.get('albumartist', ''),
      kwargs.get('compilation', ''),
      kwargs.get('conductor', ''),
      kwargs.get('catalognumber', ''),
      kwargs.get('musicip_puid', ''),
      kwargs.get('organization', ''),
      kwargs.get('composersort', ''),
      kwargs.get('artistsort', ''),
      kwargs.get('musicbrainz_discid', ''),
      kwargs.get('musicbrainz_albumtype', ''),
      kwargs.get('musicbrainz_albumstatus', ''),
      kwargs.get('musicbrainz_albumartistid', ''),
      kwargs.get('musicbrainz_trmid', ''),
      kwargs.get('musicbrainz_trackid', ''),
      kwargs.get('musicbrainz_releasetrackid', ''),
      kwargs.get('musicbrainz_artistid', ''),
      kwargs.get('musicbrainz_albumid', ''),
      kwargs.get('musicbrainz_workid', ''),
      kwargs.get('musicbrainz_releasegroupid', ''),
      kwargs.get('bpm', ''),
      kwargs.get('titlesort', ''),
      kwargs.get('acoustid_id', ''),
      kwargs.get('language', ''),
      kwargs.get('encodedby', ''),
      kwargs.get('barcode', ''),
      kwargs.get('composer', ''),
      kwargs.get('albumartist_sort', ''),
      kwargs.get('albumartist_credit', ''),
      kwargs.get('length', ''),
      kwargs.get('performer', ''),
      kwargs.get('musicip_fingerprint', ''),
      kwargs.get('arranger', ''),
      kwargs.get('website', 'http://google.com'),
      kwargs.get('version', ''),
      kwargs.get('isrc', ''),
      kwargs.get('disctitle', ''),
      kwargs.get('discnumber', ''),
      kwargs.get('lyricist', ''),
      kwargs.get('acoustid_fingerprint', ''),
      kwargs.get('tracknumber', ''),
      kwargs.get('original_year', ''),
      kwargs.get('original_month', ''),
      kwargs.get('original_day', ''),
      kwargs.get('format', ''),
      kwargs.get('asin', ''),
      kwargs.get('channels', ''),
      kwargs.get('bitrate', ''),
      kwargs.get('samplerate', ''),
      kwargs.get('bitdepth', ''),
      kwargs.get('rg_track_gain', ''),
      kwargs.get('rg_track_peak', ''),
      kwargs.get('rg_album_gain', ''),
      kwargs.get('rg_album_peak', ''),
      kwargs.get('r128_album_gain', ''),
      kwargs.get('r128_track_gain', ''),
      kwargs.get('tracktotal', ''),
      kwargs.get('length', ''),
      kwargs.get('comments', ''),
      kwargs.get('disc_number', ''),
      kwargs.get('year', ''),
      kwargs.get('month', ''),
      kwargs.get('day', ''),
      # Audiad Specific Fields
      kwargs.get('discogs_url', ''),
      kwargs.get('profile', ''),
      kwargs.get('fav', '0'),
      kwargs.get('tags', ''),
      slugify(album),
      filepath,
      kwargs.get('data_url', ''),
      ''))
    db_save(con)
    song_id = curs.lastrowid
    ''' Insert table dependencies '''
    curs.execute("""INSERT INTO music_song_style(song_id, style_id) VALUES(?,?)""",
                 (int(song_id), int(style_id[0])))


def check_genre(con, genre=""):
    """ Check genre exists
    Returns:
        genre_id (int): If genre exists
        None : If genre doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup artist in db '''
    genre_id = curs.execute("""SELECT id FROM music_genre WHERE music_genre.name  = ?""", (genre,)).fetchone()
    if genre_id:
        return genre_id
    else:
        return None


def check_style(con, style=""):
    """ Check genre exists
    Returns:
        genre_id (int): If genre exists
        None : If genre doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup artist in db '''
    style_id = curs.execute("""SELECT id FROM music_style WHERE music_style.name  = ?""", (style,)).fetchone()
    if style_id:
        return style_id
    else:
        return None


def check_label(con, label=""):
    """ Check label exists
    Returns:
        label_id (int): If label exists
        None : If label doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup label in db '''
    label_id = curs.execute("""SELECT id FROM music_label WHERE music_label.name  = ?""", (label,)).fetchone()
    if label_id:
        return label_id
    else:
        return None


def check_country(con, country=""):
    """ Check country exists
    Returns:
        country_id (int): If country exists
        None : If country doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup country in db '''
    country_id = curs.execute("""SELECT id FROM music_country WHERE music_country.name  = ?""", (country,)).fetchone()
    if country_id:
        return country_id
    else:
        return None


def check_artist(con, artist=""):
    """ Check artist exists
    Returns:
        artist_id (int): If artist exists
        None : If artist doesnt
 
    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup artist in db '''
    artist_id = curs.execute("""SELECT id FROM music_artist WHERE music_artist.name  = ?""", (artist,)).fetchone()
    if artist_id:
        print(artist_id)
        return artist_id
    else:
        return None


def check_album(con, album="", artist=""):
    """ Check album exists
    Returns:
        album_id (int): If album exists
        None : If album doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup album in db '''
    album_id = curs.execute("""SELECT id FROM music_album WHERE music_album.title = ?""", (album,)).fetchone()
    album_artist = curs.execute("""SELECT artist_id FROM music_album WHERE music_album.title = ?""", (album,)).fetchone()
    if album_id:
        ''' Lookup artist in db '''
        #if album_artist == check_artist(con, artist):
        return album_id
    else:
        return None


def check_song(con, song="", artist="", album=""):
    """ Check song exists
        Returns:
            song_id (int): If song exists
            None : If song doesnt

    """
    curs = con.cursor()
    curs.execute("""PRAGMA foreign_keys=ON""")
    ''' Lookup song in db '''
    song_id = curs.execute(
        """SELECT id FROM music_song WHERE music_song.title = ?""", (song,)).fetchone()
    song_artist = curs.execute(
        """SELECT artist_id FROM music_song WHERE music_song.title = ?""", (song,)).fetchone()
    album_id = curs.execute(
        """SELECT album_id FROM music_song WHERE music_song.title = ?""", (song,)).fetchone()
    if song_id:
        # ''' Lookup artist in db '''
        # if song_artist == check_artist(con, artist):
        #     ''' Lookup album in db '''
        #     if album_id == check_album(con, album, artist):
        return song_id
    else:
        return None


# artist.save()


# allocate path -> scan path for files -> determine audio formats -> yield: path, media file
#   -> create song object with file -> read metadata -> check for existing entry -> save data
def audio_files(root):
    """ Print files in movie_directory with extensions in movie_extensions, recursively. """

    # Get the absolute path of the path parameter
    root = os.path.abspath(root)

    # Get a list of files in audio directory
    directory_files = os.listdir(root)

    # Traverse through all files
    for filename in directory_files:
        filepath = os.path.join(root, filename)

        # Check if it's a normal file or directory
        if os.path.isfile(filepath):

            # Check if the file has an extension of typical audio files
            for extension in MEDIA_FORMATS:
                # Not a audio file, ignore
                if not filepath.endswith(extension):
                    continue
                # We have got a audio file, Increment the counter
                audio_files.counter += 1
                # Print it's name
                process_file(filepath)

        elif os.path.isdir(filepath):
            # We got a directory, enter into it for further processing
            audio_files(filepath)


def process_file(filepath):
    item = Item(filepath)
    ''' Connect to database'''
    try:
        db = get_db(DATABASE)
    except FileNotFoundError:
        print('File Error. Please check the location\n' + DATABASE)
        return None
    except ConnectionError:
        print('Database Conncetion Error. Please Check settings')
        return None

    print('Connection ' + str(db) + ' Established')
    genre = item.genre()
    style = item.style()
    country = item.country()
    label = item.label()
    artist = item.artist()
    album = item.album()
    song = item.song()
    ret = False
    if artist is '<unknown>' or artist is None:
        print('Artist Error')
        ret = True
    if album is '<unknown>' or None:
        print('Artist Error')
        ret = True
    if song is '<unknown>' or None:
        print('Song Error')
        ret = True
    if ret is False:
        ''' checking Genre '''
        temp_pk = check_genre(db, genre=genre)
        if not temp_pk:
            print(genre + ' - is not in the database. ADDING\n')
            add_genre(db, name=genre)
            db_save(db)
            print('added ' + str(genre))
        if temp_pk:
            print(genre + ' - is already in the database. PASSING\n')

        ''' checking Style '''
        temp_pk = check_style(db, style=style)
        if not temp_pk:
            print(style + ' - is not in the database. ADDING\n')
            add_style(db, name=style)
            db_save(db)
            print('added ' + str(style))
        if temp_pk:
            print(style + ' - is already in the database. PASSING\n')

        ''' checking Country '''
        temp_pk = check_country(db, country=country)
        if not temp_pk:
            print(country + ' - is not in the database. ADDING\n')
            add_country(db, name=country)
            db_save(db)
        if temp_pk:
            print(country + ' - is already in the database. PASSING\n')

        ''' checking Label '''
        temp_pk = check_label(db, label=label)
        if not temp_pk:
            print(label + ' - is not in the database. ADDING\n')
            add_label(db, name=label)
            db_save(db)
        if temp_pk:
            print(label + ' - is already in the database. PASSING\n')

        ''' checking Artist '''
        temp_pk = check_artist(db, artist=artist)
        if not temp_pk:
            print(artist + ' - is not in the database. ADDING\n')
            print(item.get_artist())
            add_artist(db, countrys=country, genres=genre, styles=style, **item.get_artist())
            db_save(db)
        if temp_pk:
            print(artist + ' - is already in the database. PASSING\n')

        ''' checking Album '''
        temp_pk = check_album(db, album=album, artist=artist)
        if not temp_pk:
            print(album + ' - is not in the database. ADDING\n')
            add_album(db, genres=genre, styles=style, artist=artist, labels=label, countrys=country, **item.get_album())
            db_save(db)
        if temp_pk:
            print(album + ' - is already in the database. PASSING\n')

        ''' checking Song '''
        temp_pk = check_song(db, song=song, album=album, artist=artist)
        if not temp_pk:
            print(song + ' - is not in the database. ADDING\n')
            add_song(db, filepath, genres=genre, labels=label, countrys=country, styles=style, song=song, **item.get_song())
            db_save(db)
        if temp_pk:
            print(song + ' - is already in the database. PASSING\n')


if __name__ == '__main__':

    # Directory argument supplied, check and use if it's a directory
    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            path = sys.argv[1]
        else:
            print('ERROR: "{0}" is not a directory.'.format(sys.argv[1]))
            exit(1)
    else:
        # Set our movie directory to the current working directory
        path = os.getcwd()
    print('\n -- Looking for audio files in "{0}" --\n'.format(path))
    # Set the number of processed files equal to zero
    audio_files.counter = 0
    # Start Processing
    audio_files(path)
    # We are done. Exit now.
    print('\n -- {0} Audio File(s) found in directory {1} --'.format(audio_files.counter, path))
    print('\nPress ENTER to exit!')
    # Wait until the user presses enter/return, or <CTRL-C>
    try:
        input()
    except KeyboardInterrupt:
        exit(0)
