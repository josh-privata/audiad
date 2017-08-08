import os
from mutagen.id3 import ID3
from musicimport import db_connect


def mp3_files():
    # this is a generator that will return mp3 file paths within given dir
    root = '/storage/media/music'
    genre = ""
    artist = ""
    db_connect.addcountry("P")
    for g in os.listdir(root):
        if not g.startswith('.'):
            if os.path.isdir(os.path.join(root, g)):
                genre = g
                db_connect.addgenre(genre)
            roots = os.path.join(root, g)
            for a in os.listdir(roots):
                if not a.startswith('.'):
                    if os.path.isdir(os.path.join(roots, a)):
                        if str(genre) is not "Compilations" or "Soundtracks" or "Youtube" or "Podcasts" or "playlists":
                            artist = a
                            db_connect.addartist(genre, artist)
                            rootss = os.path.join(roots, a)
                            if os.path.isdir(rootss):
                                for al in os.listdir(rootss):

                                        if os.path.isdir(os.path.join(rootss, al)):
                                            album = al
                                            db_connect.addalbum(genre, artist, album)
                                            rootsss = os.path.join(rootss, al)
                                            if os.path.isdir(rootsss):
                                                for s in os.listdir(rootsss):
                                                    if not al.startswith('.'):
                                                        if os.path.isfile(os.path.join(rootsss, s)):
                                                            if s.endswith(".mp3") or s.endswith(".flac"):
                                                                song = s
                                                                db_connect.addsong(genre, artist, album, song)

if __name__ == "__main__":
    mp3_files()
#
#
# class IterMixin(object):
#     def __iter__(self):
#         for attr, value in self.__dict__.items():
#             yield attr, value
#
#
# class gettags(IterMixin):
#
#     def __init__(self, file):
#         audio = ID3(file)
#         picture = audio["APIC"].text[0]
#         picture1 = audio['APIC-1'].text[0]
#         picture2 = audio["APIC-2"].text[0]
#         picture3 = audio["APIC-3"].text[0]
#         comment = audio["COMM"].text[0]
#         itunes = audio['ITNU'].text[0]
#         musiccdidentifier = audio["MCDI"].text[0]
#         ownership = audio["OWNE"].text[0]
#         playcounter = audio["PCNT"].text[0]
#         podcast = audio['PCST'].text[0]
#         popularimeter = audio["POPM"].text[0]
#         private = audio["PRIV"].text[0]
#         relativevolumeadjustment = audio["RVA2"].text[0]
#         synlyrics = audio['SYLT'].text[0]
#         album = audio["TALB"].text[0]
#         bpm = audio["TBPM"].text[0]
#         podcastcategory = audio["TCAT"].text[0]
#         compilation = audio['TCMP'].text[0]
#         composer = audio["TCOM"].text[0]
#         genre = audio["TCON"].text[0]
#         copyright = audio["TCOP"].text[0]
#         encodingtime = audio['TDEN'].text[0]
#         podcastdescription = audio["TDES"].text[0]
#         playlistdelay = audio["TDLY"].text[0]
#         originalreleasetime = audio["TDOR"].text[0]
#         recordingtime = audio['TDRC'].text[0]
#         releasetime = audio["TDRL"].text[0]
#         taggingtime = audio["TDTG"].text[0]
#         encodedby = audio["TENC"].text[0]
#         lyricist = audio['TEXT'].text[0]
#         filetype = audio["TFLT"].text[0]
#         podcastid = audio["TGID"].text[0]
#         involvedpeople = audio["TIPL"].text[0]
#         grouping = audio['TIT1'].text[0]
#         title = audio["TIT2"].text[0]
#         subtitle = audio["TIT3"].text[0]
#         initialkey = audio["TKEY"].text[0]
#         podcastkeywords = audio['TKWD'].text[0]
#         language = audio["TLAN"].text[0]
#         length = audio["TLEN"].text[0]
#         musiciancredits = audio["TMCL"].text[0]
#         media = audio['TMED'].text[0]
#         mood = audio["TMOO"].text[0]
#         originalalbum = audio["TOAL"].text[0]
#         originalfilename = audio["TOFN"].text[0]
#         originallyricist = audio['TOLY'].text[0]
#         originalartist = audio["TOPE"].text[0]
#         fileowner = audio["TOWN"].text[0]
#         artist = audio["TPE1"].text[0]
#         band = audio['TPE2'].text[0]
#         conductor = audio["TPE3"].text[0]
#         interpretedby = audio["TPE4"].text[0]
#         partofset = audio["TPOS"].text[0]
#         producednotice = audio['TPRO'].text[0]
#         publisher = audio["TPUB"].text[0]
#         track = audio["TRCK"].text[0]
#         internetradiostationname = audio["TRSN"].text[0]
#         internetradiostationowner = audio['TRSO'].text[0]
#         albumartistsortorder = audio["TSO2"].text[0]
#         albumsortorder = audio["TSOA"].text[0]
#         composersortorder = audio["TSOC"].text[0]
#         performersortorder = audio['TSOP'].text[0]
#         titlesortorder = audio["TSOT"].text[0]
#         tsrc = audio["TSRC"].text[0]
#         encoder_settings = audio["TSSE"].text[0]
#         setsubtitle = audio['TSST'].text[0]
#         userdefinedtext = audio["TXXX"].text[0]
#         termsofuse = audio["USER"].text[0]
#         lyrics = audio["USLT"].text[0]
#         commercialURL = audio['WCOM'].text[0]
#         copyrightURL = audio["WCOP"].text[0]
#         podcastURL = audio["WFED"].text[0]
#         fileURL = audio["WOAF"].text[0]
#         artistURL = audio['WOAR'].text[0]
#         sourceURL = audio["WOAS"].text[0]
#         internetradiostationURL = audio["WORS"].text[0]
#         paymentURL = audio["WPAY"].text[0]
#         publisherURL = audio["WPUB"].text[0]
#         userdefinedURL = audio["WXXX"].text[0]
#         originalreleasetime = audio["XDOR"].text[0]
#         olympusDSS = audio["XOLY"].text[0]
#         albumsortorder = audio["XSOA"].text[0]
#         performersortorder = audio["XSOP"].text[0]
#         titlesortorder = audio["XSOT"].text[0]


