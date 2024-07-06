from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import (
    CustomUserViewSet, ArtistProfileViewSet, SongViewSet, PlaylistViewSet, FavoriteViewSet,
    home, register, login_view, artist_profile, upload_song, create_playlist, playlists,
    playlist_detail, favorites, search_songs
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'artists', ArtistProfileViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('artist_profile/', artist_profile, name='artist_profile'),
    path('upload_song/', upload_song, name='upload_song'),
    path('create_playlist/', create_playlist, name='create_playlist'),
    path('playlists/', playlists, name='playlists'),
    path('playlist/<int:playlist_id>/', playlist_detail, name='playlist_detail'),
    path('favorites/', favorites, name='favorites'),
    path('search/', search_songs, name='search_songs'),
    path('api/', include(router.urls)),
]
