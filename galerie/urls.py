from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galerie/', views.upload_artwork, name='upload_artwork'),
    path('galerie/edit/<int:pk>/', views.edit_artwork, name='edit_artwork'),
    path('galerie/delete/<int:pk>/', views.delete_artwork, name='delete_artwork'),
    path('artist/', views.artist_profile, name='artist_profile'),
    path('artist/edit/', views.edit_profile, name='edit_profile'),
    path('datenschutz/', views.privacy, name='privacy'),  
]
