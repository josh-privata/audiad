import os

import sqlite3
from mutagen.id3 import ID3


def mp3_files():
    # this is a generator that will return mp3 file paths within given dir
    root = '/storage/media/music'
    genre = ""
    artist = ""
    for g in os.listdir(root):
        if not g.startswith('.'):
            if os.path.isdir(os.path.join(root, g)):
                genre = g
                addgenre(genre)
            roots = os.path.join(root, g)
            for a in os.listdir(roots):
                if not a.startswith('.'):
                    if os.path.isdir(os.path.join(roots, a)):
                        if str(genre) is not "Compilations" or "Soundtracks" or "Youtube" or "Podcasts" or "playlists":
                            artist = a
                            addartist(genre, artist)
                            rootss = os.path.join(roots, a)
                            if os.path.isdir(rootss):
                                for al in os.listdir(rootss):

                                        if os.path.isdir(os.path.join(rootss, al)):
                                            album = al
                                            addalbum(genre, artist, album)
                                            rootsss = os.path.join(rootss, al)
                                            if os.path.isdir(rootsss):
                                                for s in os.listdir(rootsss):
                                                    if not al.startswith('.'):
                                                        if os.path.isfile(os.path.join(rootsss, s)):
                                                            if s.endswith(".mp3") or s.endswith(".flac"):
                                                                song = s
                                                                addsong(genre, artist, album, song)


def addgenre(genre):
    con = sqlite3.connect("/home/josh/Code/django/djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        # cur.execute("""DELETE FROM music_album_genre""")
        # cur.execute("""DELETE FROM music_genre""")
        # cur.execute("""DELETE FROM music_album""")
        # cur.execute("""DELETE FROM music_artist""")
        cur.execute("""INSERT INTO music_genre(name, fav) VALUES(?,?)""", (genre, '0',))
    con.commit()
    con.close()


def addartist(genre, artist):
    con = sqlite3.connect("/home/josh/Code/django/djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genre,)).fetchone()
        cur.execute("""INSERT INTO music_artist(name, country, slug, realname, profile, fav, discogs_url)
                       VALUES(?, ?, ?, ?, ?, ?, ?)""",
                       (artist, '0', '0', '0', '0', '0', '0',))
        aid = cur.lastrowid
        cur.execute("""INSERT INTO music_artist_genre(artist_id, genre_id) VALUES(?,?)""", (int(aid), int(gid[0])))
    con.commit()
    con.close()


def addalbum(genre, artist, album):
    con = sqlite3.connect("/home/josh/Code/django/djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genre,)).fetchone()
        mid = cur.execute("""SELECT id FROM music_artist WHERE music_artist.name = ?""", (artist,)).fetchone()
        user = 1
        if gid and mid:
            cur.execute("""INSERT INTO music_album(title, artist_id, user_id, profile, subtitle, producer, date, country, year, cover, discogs_url, fav, slug)
                           VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (album, int(mid[0]), int(user), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',))
            aid = cur.lastrowid

            cur.execute("""INSERT INTO music_album_genre(album_id, genre_id) VALUES(?,?)""", (int(aid), int(gid[0])))
    con.commit()
    con.close()


def addsong(genre, artist, album, song):
    con = sqlite3.connect("/home/josh/Code/django/djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name  = ?""", (genre,)).fetchone()
        mid = cur.execute("""SELECT id FROM music_artist WHERE music_artist.name  = ?""", (artist,)).fetchone()
        aid = cur.execute("""SELECT id FROM music_album WHERE music_album.title = ?""", (album,)).fetchone()
        if gid and mid and aid:
            cur.execute("""INSERT INTO music_song(title, album_id, artist_id, producer, profile, track, fav, length, audio_file, last_played, discogs_url, slug)
 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (os.path.splitext(song)[0], int(aid[0]), int(mid[0]), '0', '0', '0', '0', '0', '0', '0', '0', '0',))
            sid = cur.lastrowid
            cur.execute("""INSERT INTO music_song_genre(song_id, genre_id) VALUES(?, ?)""", (int(sid), int(gid[0])))
    con.commit()
    con.close()

if __name__ == '__main__':
    mp3_files()