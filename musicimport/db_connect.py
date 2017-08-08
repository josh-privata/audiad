import os
import sqlite3


def addcountry(country):
    con = sqlite3.connect("/home/josh/Code/django/Djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        cur.execute("""INSERT INTO music_country(name) VALUES(?)""", country)
        cur.execute("""INSERT INTO music_label(name, discogs_url, fav, profile, parent, website, logo, slug) 
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", ('p', '0', '0', '0', '0', '0', '0', '0'))
    con.commit()
    con.close()


def addgenre(genre):
    con = sqlite3.connect("/home/josh/Code/django/Djangles/mydatabase")
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
    con = sqlite3.connect("/home/josh/Code/django/Djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genre,)).fetchone()
        cur.execute("""INSERT INTO music_artist(name, country_id, slug, realname, profile, fav, discogs_url)
                       VALUES(?, ?, ?, ?, ?, ?, ?)""",
                       (artist, '1', '0', '0', '0', '0', '0',))
        aid = cur.lastrowid
        cur.execute("""INSERT INTO music_artist_genre(artist_id, genre_id) VALUES(?,?)""", (int(aid), int(gid[0])))
    con.commit()
    con.close()


def addalbum(genre, artist, album):
    con = sqlite3.connect("/home/josh/Code/django/Djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name = ?""", (genre,)).fetchone()
        mid = cur.execute("""SELECT id FROM music_artist WHERE music_artist.name = ?""", (artist,)).fetchone()
        user = 1
        label = 1
        if gid and mid:
            cur.execute("""INSERT INTO music_album(title, genre_id, artist_id, user_id, label_id, country_id, profile, subtitle, producer, date, data_url, data_source, catalognum, releasegroup_id, albumtype, mediums, tracks, day,  month, year, cover, discogs_url, fav, slug)
                           VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?)""",
                           (album, int(gid[0]), int(mid[0]), int(user), int(label), int(label), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',))
    con.commit()
    con.close()


def addsong(genre, artist, album, song):
    con = sqlite3.connect("/home/josh/Code/django/Djangles/mydatabase")
    with con:
        cur = con.cursor()
        cur.execute("""PRAGMA foreign_keys=ON""")
        gid = cur.execute("""SELECT id FROM music_genre WHERE music_genre.name  = ?""", (genre,)).fetchone()
        mid = cur.execute("""SELECT id FROM music_artist WHERE music_artist.name  = ?""", (artist,)).fetchone()
        aid = cur.execute("""SELECT id FROM music_album WHERE music_album.title = ?""", (album,)).fetchone()
        if gid and mid and aid:
            cur.execute("""INSERT INTO music_song(title, album_id, artist_id, genre_id, data_source, disc_number, profile, track, fav, "index", length, audio_file, last_played, discogs_url, slug)
 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            os.path.splitext(song)[0], int(aid[0]), int(mid[0]), int(gid[0]), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',))
    con.commit()
    con.close()