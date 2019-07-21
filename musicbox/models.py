from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a song gerne (e.g. Hiphop)', primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail', args=[str(self.name)])

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Artist(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100, primary_key=True)
    real_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    link = models.URLField(default='https://search.naver.com/search.naver?query=')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.name)])

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)

    artist = models.ManyToManyField(Artist)

    link = models.CharField(max_length=1000, help_text='Enter a youtube video ID of this song')

    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title', 'genre']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])

    def display_artist(self):
        return ', '.join(artist.name for artist in self.artist.all()[:3])

        display_artist.short_description = 'Artist'

class Playlist(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    explanation = models.TextField(max_length=1000, help_text='Enter a explanation of this song')
    songs = models.ManyToManyField(Song, help_text='Select a songs for this playlist')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('playlist_detail', args=[str(self.name)])

    def display_song(self):
        return ', '.join(song.title for song in self.songs.all()[:3])

        display_song.short_description = 'Song'
