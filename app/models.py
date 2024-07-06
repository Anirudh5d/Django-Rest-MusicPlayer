from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    is_artist = models.BooleanField(default=False)
    
class ArtistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    
class Song(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='songs')
    year_of_release = models.PositiveIntegerField()
    file = models.FileField(upload_to="songs/")
    
class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="playlist")
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song)
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorite')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    