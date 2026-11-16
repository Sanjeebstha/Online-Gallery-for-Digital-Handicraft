from django import forms
from .models import ArtworkImage, ArtistProfile

class ArtworkImageForm(forms.ModelForm):
    class Meta:
        model = ArtworkImage
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter artwork name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your artwork'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['bio', 'profile_picture', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Tell visitors about yourself and your art...'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://yourwebsite.com'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }