from django.shortcuts import render, get_object_or_404
from .models import Genre, Artist, Song, Playlist
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    num_songs = Song.objects.all().count()
    num_playlists = Playlist.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_artists = Artist.objects.all().count()

    context = {
        'num_songs': num_songs,
        'num_artists': num_artists,
        'num_genres': num_genres,
        'num_playlists': num_playlists,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'musicbox/index.html', context=context)

# Create your views here.
def song_list(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 5)
    page = request.GET.get('page')
    songs = paginator.get_page(page)

    return render(request, 'musicbox/song_list.html', {'contexts': songs})

def artist_list(request):
    artist_list = Artist.objects.all()
    paginator = Paginator(artist_list, 10)
    page = request.GET.get('page')
    artists = paginator.get_page(page)

    return render(request, 'musicbox/artist_list.html', {'contexts': artists})

def genre_list(request):
    genre_list = Genre.objects.all()
    paginator = Paginator(genre_list, 10)
    page = request.GET.get('page')
    genres = paginator.get_page(page)

    return render(request, 'musicbox/genre_list.html', {'contexts': genres})

def playlist_list(request):
    playlist_list = Playlist.objects.all()
    paginator = Paginator(playlist_list, 10)
    page = request.GET.get('page')
    playlists = paginator.get_page(page)

    return render(request, 'musicbox/playlist_list.html', {'contexts': playlists})

def artist_detail(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    song_list = Song.objects.filter(artist=artist_name)
    paginator = Paginator(song_list, 5)
    page = request.GET.get('page')
    songs = paginator.get_page(page)

    return render(request, 'musicbox/artist_detail.html', {'contexts': songs, 'artist' : artist})

def genre_detail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    song_list = Song.objects.filter(genre=genre_name)
    paginator = Paginator(song_list, 5)
    page = request.GET.get('page')
    songs = paginator.get_page(page)

    return render(request, 'musicbox/genre_detail.html', {'contexts': songs, 'genre' : genre})

def playlist_detail(request, playlist_name):
    playlist = get_object_or_404(Playlist, name=playlist_name)
    song_list = playlist.songs.all()
    paginator = Paginator(song_list, 5)
    page = request.GET.get('page')
    songs = paginator.get_page(page)

    return render(request, 'musicbox/playlist_detail.html', {'contexts': songs, 'playlist' : playlist})
