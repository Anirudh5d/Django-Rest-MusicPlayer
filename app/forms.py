from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ArtistProfile, Song, Playlist

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'is_artist', 'password1', 'password2')

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['bio']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'genre', 'year_of_release', 'file']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
