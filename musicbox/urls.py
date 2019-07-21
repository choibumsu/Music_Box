from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs', views.song_list, name='song_list'),
    path('artists', views.artist_list, name='artist_list'),
    path('genres', views.genre_list, name='genre_list'),
    path('playlists', views.playlist_list, name='playlist_list'),

    path('artists/<str:artist_name>', views.artist_detail, name='artist_detail'),
    path('genres/<str:genre_name>', views.genre_detail, name='genre_detail'),
    path('playlists/<str:playlist_name>', views.playlist_detail, name='playlist_detail'),
]
