from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, ArtistProfile, Song, Playlist, Favorite
from .serializers import CustomUserSerializer, ArtistProfileSerializer, SongSerializer, PlaylistSerializer, FavoriteSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ArtistProfileForm, SongForm, PlaylistForm
from .models import Playlist, Favorite, Song

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



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



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
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = request.user
            song.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'upload_song.html', {'form': form})

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

@login_required
def playlists(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlist.html', {'playlists': playlists})

@login_required
def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'playlist_detail.html', {'playlist': playlist})

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

def search_songs(request):
    query = request.GET.get('query', '')
    songs = Song.objects.filter(name__icontains=query) | Song.objects.filter(genre__icontains=query) | Song.objects.filter(artist__username__icontains=query)
    return render(request, 'search.html', {'songs': songs, 'query': query})
