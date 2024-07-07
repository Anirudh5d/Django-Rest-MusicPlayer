from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, ArtistProfile, Song, Playlist, Favorite
from .serializers import CustomUserSerializer, ArtistProfileSerializer, SongSerializer, PlaylistSerializer, FavoriteSerializer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ArtistProfileForm, SongForm, PlaylistForm
from .models import Playlist, Favorite, Song
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Q
from .forms import CustomUserCreationForm, SongUploadForm


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class ArtistProfileViewSet(viewsets.ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    permission_classes = [IsAuthenticated]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]




@login_required
def add_to_favorites(request, song_id):
    song = Song.objects.get(id=song_id)
    Favorite.objects.create(user=request.user, song=song)
    return redirect('home')

@login_required
def add_to_playlist(request, song_id):
    song = Song.objects.get(id=song_id)
    playlist, created = Playlist.objects.get_or_create(user=request.user, name='My Playlist')
    playlist.songs.add(song)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.user.is_artist and song.artist == request.user:
        song.delete()
    return redirect('home')

@login_required
def artist_profile(request):
    return render(request, 'artist_profile.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})

@login_required
def upload_song(request):
    if not request.user.is_artist:
        return redirect('home')
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = request.user
            song.save()
            return redirect('home')
    else:
        form = SongUploadForm()
    return render(request, 'upload_song.html', {'form': form})

def search_songs(request):
    query = request.GET.get('q')
    search_results = Song.objects.filter(title__icontains=query)
    context = {
        'search_results': search_results,
        'query': query,
    }
    return render(request, 'home.html', context)

@login_required
def playlists(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists.html', {'playlists': playlists})

@login_required
def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'playlist_detail.html', {'playlist': playlist})

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})





@login_required
def artist_profile(request):
    if request.method == 'POST':
        form = ArtistProfileForm(request.POST, instance=request.user.artistprofile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistProfileForm(instance=request.user.artistprofile)
    return render(request, 'artist_profile.html', {'form': form})


@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('playlists')
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})


