from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     tags = TaggableManager(blank=True)
#     genres = models.ManyToManyField(Genre, blank=True, default=None)
#     styles = models.ManyToManyField(Style, blank=True, default=None)
#     artists = models.ManyToManyField(Artist, blank=True, default=None)
#     songs = models.ManyToManyField(Song, blank=True, default=None)
#     labels = models.ManyToManyField(Label, blank=True, default=None)
#     albums = models.ManyToManyField(Album, blank=True, default=None)


#     def __str__(self):
#         return self.bio


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()


# class mp3tag(models.Model):
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)
#      = models.CharField("tracknumber", max_length=50, blank=True)
#      = models.CharField("discnumber", max_length=50, blank=True)
#      = models.CharField("totaldiscs", max_length=50, blank=True)
#      = models.CharField("totaltracks", max_length=50, blank=True)
#      = models.CharField("title", max_length=50, blank=True)
#      = models.CharField("titlesortorder", max_length=50, blank=True)
#      = models.CharField("album", max_length=50, blank=True)
#      = models.CharField("albumsortorder", max_length=50, blank=True)
#      = models.CharField("origalbum", max_length=50, blank=True)
#      = models.CharField("subtitle", max_length=50, blank=True)
#      = models.CharField("setsubtitle", max_length=50, blank=True)
#      = models.CharField("artist", max_length=50, blank=True)
#      = models.CharField("performersortorder", max_length=50, blank=True)
#      = models.CharField("wwwartist", max_length=50, blank=True)
#      = models.CharField("origartist", max_length=50, blank=True)
#      = models.CharField("band", max_length=50, blank=True)
#      = models.CharField("composer", max_length=50, blank=True)
#      = models.CharField("lyricist", max_length=50, blank=True)
#      = models.CharField("origlyricist", max_length=50, blank=True)
#      = models.CharField("conductor", max_length=50, blank=True)
#      = models.CharField("mixartist", max_length=50, blank=True)
#      = models.CharField("publisher", max_length=50, blank=True)
#     wwwpublisher = models.CharField(max_length=50, blank=True)
#     encodedby = models.CharField(max_length=50, blank=True)
#     involvedpeople = models.CharField(max_length=50, blank=True)
#     musiciancreditlist = models.CharField(max_length=50, blank=True)
#     genre = models.CharField(max_length=50, blank=True)
#     mood = models.CharField(max_length=50, blank=True)
#     mediatype = models.CharField(max_length=50, blank=True)
#     wwwaudiosource = models.CharField(max_length=50, blank=True)
#     language = models.CharField(max_length=50, blank=True)
#     contentgroup = models.CharField(max_length=50, blank=True)
#     recordingtime = models.CharField(max_length=50, blank=True)
#     releasetime = models.CharField(max_length=50, blank=True)
#     encodingtime = models.CharField(max_length=50, blank=True)
#     taggingtime = models.CharField(max_length=50, blank=True)
#     origreleasetime = models.CharField(max_length=50, blank=True)
#     comment = models.CharField(max_length=50, blank=True)
#     popularimeter = models.CharField(max_length=50, blank=True)
#     playcounter = models.CharField(max_length=50, blank=True)
#     encodersettings = models.CharField(max_length=50, blank=True)
#     songlen = models.CharField(max_length=50, blank=True)
#     filetype = models.CharField(max_length=50, blank=True)
#     seekframe = models.CharField(max_length=50, blank=True)
#     mpeglookup = models.CharField(max_length=50, blank=True)
#     audioseekpoint = models.CharField(max_length=50, blank=True)
#     playlistdelay = models.CharField(max_length=50, blank=True)
#     eventtiming = models.CharField(max_length=50, blank=True)
#     syncedtempo = models.CharField(max_length=50, blank=True)
#     positionsync = models.CharField(max_length=50, blank=True)
#     buffersize = models.CharField(max_length=50, blank=True)
#     bpm = models.CharField(max_length=50, blank=True)
#     initialkey = models.CharField(max_length=50, blank=True)
#     volumeadj = models.CharField(max_length=50, blank=True)
#     reverb = models.CharField(max_length=50, blank=True)
#     equalizations = models.CharField(max_length=50, blank=True)
#     isrc = models.CharField(max_length=50, blank=True)
#     cdid = models.CharField(max_length=50, blank=True)
#     uniquefileid = models.CharField(max_length=50, blank=True)
#     wwwcommercialinfo = models.CharField(max_length=50, blank=True)
#     wwwpayment = models.CharField(max_length=50, blank=True)
#     fileowner = models.CharField(max_length=50, blank=True)
#     commercial = models.CharField(max_length=50, blank=True)
#     copyright = models.CharField(max_length=50, blank=True)
#     producednotice = models.CharField(max_length=50, blank=True)
#     termsofuse = models.CharField(max_length=50, blank=True)
#     wwwcopyright = models.CharField(max_length=50, blank=True)
#     ownership = models.CharField(max_length=50, blank=True)
#     audiocrypto = models.CharField(max_length=50, blank=True)
#     cryptoreg = models.CharField(max_length=50, blank=True)
#     groupingreg = models.CharField(max_length=50, blank=True)
#     signature = models.CharField(max_length=50, blank=True)
#     unsyncedlyrics = models.CharField(max_length=50, blank=True)
#     syncedlyrics = models.CharField(max_length=50, blank=True)
#     picture = models.CharField(max_length=50, blank=True)
#     generalobject = models.CharField(max_length=50, blank=True)
#     private = models.CharField(max_length=50, blank=True)
#     usertext = models.CharField(max_length=50, blank=True)
#     linkedinfo = models.CharField(max_length=50, blank=True)
#     origfilename = models.CharField(max_length=50, blank=True)
#     netradiostation = models.CharField(max_length=50, blank=True)
#     netradioowner = models.CharField(max_length=50, blank=True)
#     wwwradiopage = models.CharField(max_length=50, blank=True)
#     wwwuser = models.CharField(max_length=50, blank=True)
#     wwwaudiofile = models.CharField(max_length=50, blank=True)

    # @property
    # def __str__(self):
    #     return self.song


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)
    fav = models.BooleanField(default=False, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, default=None)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    tags = TaggableManager(blank=True)
    fav = models.BooleanField(default=False, blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Style, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False)
    realname = models.CharField(max_length=200, blank=True, null=True, default=None)
    profile = models.CharField(max_length=2000, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True, default=None)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
    genre = models.ManyToManyField(Genre, blank=True, default=None)
    country = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=200, blank=True, default=None, null=True)
    discogs_url = models.URLField(max_length=200, blank=True, null=True)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
    profile = models.CharField(max_length=2000, blank=True, default="", null=True)
    contact = models.CharField(max_length=200, blank=True, null=True, default=None)
    parent = models.CharField(max_length=200, blank=True, null=True, default=None)
    website = models.URLField(max_length=200, blank=True, null=True, default=None)
    logo = models.FileField(null=True, blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Label, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    profile = models.CharField(max_length=2000, blank=True, default="")
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, blank=True, default=None)
    genre = models.ManyToManyField(Genre, blank=True, default="")
    style = models.ManyToManyField(Style, blank=True, default="")
    label = models.ManyToManyField(Label, blank=True, default="")
    title = models.CharField(max_length=500, blank=False)
    subtitle = models.CharField(max_length=500, blank=True)
    producer = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True, default=None)
    country = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(null=True, blank=True, default=None)
    cover = models.FileField(null=True, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True)
    fav = models.BooleanField(default=False, blank=True)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True)
    profile = models.CharField(max_length=2000, blank=True, default="")
    discogs_url = models.URLField(max_length=200, blank=True, null=True)
    style = models.ManyToManyField(Style, blank=True, default=None)
    track = models.IntegerField(null=True, blank=True, default=None)
    title = models.CharField(max_length=500, blank=False)
    fav = models.BooleanField(default=False, blank=True)
    length = models.TimeField(null=True, blank=True, default=None)
    audio_file = models.FileField(null=True, blank=True, default="")
    producer = models.CharField(max_length=200, blank=True)
    last_played = models.DateField(null=True, blank=True, default=None)
    tags = TaggableManager(blank=True)
    slug = models.CharField(max_length=250, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Create slug on object creation
        if not self.id:
            self.slug = slugify(self.name)

        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


