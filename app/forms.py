from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ArtistProfile, Song, Playlist

class CustomUserCreationForm(UserCreationForm):
    is_artist = forms.BooleanField(required=False, label="Register as Artist")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_artist')

class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'year', 'file']
class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['bio']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'year', 'file']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
