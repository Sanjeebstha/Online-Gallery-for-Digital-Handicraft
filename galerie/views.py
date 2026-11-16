from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArtworkImageForm, ArtistProfileForm
from .models import ArtworkImage, ArtistProfile

def home(request):
    artworks = ArtworkImage.objects.all()
    return render(request, 'artworks/home.html', {'artworks': artworks})

@login_required
def upload_artwork(request):
    if request.method == 'POST':
        form = ArtworkImageForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.uploaded_by = request.user
            artwork.save()
            messages.success(request, 'Artwork uploaded successfully!')
            return redirect('home')
    else:
        form = ArtworkImageForm()
    return render(request, 'artworks/myfirst.html', {'form': form})

@login_required
def edit_artwork(request, pk):
    artwork = get_object_or_404(ArtworkImage, pk=pk)
    if request.method == 'POST':
        form = ArtworkImageForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artwork updated successfully!')
            return redirect('home')
    else:
        form = ArtworkImageForm(instance=artwork)
    return render(request, 'artworks/edit_artwork.html', {'form': form, 'artwork': artwork})

@login_required
def delete_artwork(request, pk):
    artwork = get_object_or_404(ArtworkImage, pk=pk)
    if request.method == 'POST':
        artwork.delete()
        messages.success(request, 'Artwork deleted successfully!')
        return redirect('home')
    return render(request, 'artworks/delete_artwork.html', {'artwork': artwork})

def artist_profile(request):
    try:
        profile = ArtistProfile.objects.first()  # single artist site
    except ArtistProfile.DoesNotExist:
        profile = None
    return render(request, 'artworks/artist_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, created = ArtistProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ArtistProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('artist_profile')
    else:
        form = ArtistProfileForm(instance=profile)
    return render(request, 'artworks/edit_profile.html', {'form': form})

def privacy(request):
    return render(request, 'artworks/privacy.html')