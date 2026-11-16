from django.db import models
from django.contrib.auth.models import User

class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ArtworkImage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uploaded_at']