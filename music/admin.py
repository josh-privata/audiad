from django.contrib import admin
from .models import Album, Artist, Song

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
