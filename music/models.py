from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False)
    fav = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False)
    subtitle = models.CharField(max_length=500, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True, default=None)
    year = models.IntegerField(null=True, blank=True, default=None)
    cover = models.ImageField
    fav = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    track = models.IntegerField(null=True, blank=True, default=None)
    title = models.CharField(max_length=500, blank=False)
    file_format = models.CharField(max_length=10, blank=True)
    file_size = models.IntegerField(null=True, blank=True, default=None)
    length = models.TimeField(null=True, blank=True, default=None)
    fav = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.title

