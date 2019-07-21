from django.contrib import admin

# Register your models here.
from .models import Genre
from .models import Artist
from .models import Song
from .models import Playlist

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
