from django.db import models


class SongQuerySet(models.QuerySet):

    def mp3(self):
        return self.filter(file_type='mp3')

    def smaller_than(self, size):
        return self.filter(size__lt=size)


class SongManager(models.Manager):

    def get_queryset(self):
        return SongQuerySet(self.model, using=self._db)

    def mp3(self):
        return self.get_queryset().mp3()

    def smaller_than(self, size):
        return self.get_queryset().smaller_than(size)
