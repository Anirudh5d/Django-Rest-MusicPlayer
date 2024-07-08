from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import ( 
    CustomUserViewSet, ArtistProfileViewSet, SongViewSet, PlaylistViewSet, FavoriteViewSet,
    home, register, login_view, artist_profile, upload_song, create_playlist, playlists,
    playlist_detail, delete_song, favorites, search_songs, logout_view, add_to_favorites, add_to_playlist)

from django.contrib.auth import views as auth_views
from app import views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'artists', ArtistProfileViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('artist_profile/', artist_profile, name='artist_profile'),
    path('upload_song/', upload_song, name='upload_song'),
    path('add_to_favorites/<int:song_id>/', add_to_favorites, name='add_to_favorites'),
    path('add_to_playlist/<int:song_id>/', add_to_playlist, name='add_to_playlist'),
    path('create_playlist/', create_playlist, name='create_playlist'),
    path('playlists/', playlists, name='playlists'),
    path('playlist/<int:playlist_id>/', playlist_detail, name='playlist_detail'),
    path('favorites/', favorites, name='favorites'),
    path('search/', search_songs, name='search_songs'),
    path('api/', include(router.urls)),
    path('delete_song/<int:song_id>/', delete_song, name='delete_song'),
]
