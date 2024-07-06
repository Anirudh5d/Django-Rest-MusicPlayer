from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ArtistProfileViewSet, SongViewSet, PlaylistViewSet, FavoriteViewSet
from .views import RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'artists', ArtistProfileViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'favorites', FavoriteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
