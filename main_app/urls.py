from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mymusic/', views.mymusic, name='music'),
  path('discover/', views.discover, name='discover'),
  path('mymusic/new', views.new, name='new'),
  path('mymusic/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
  path('mymusic/<int:playlist_id>/', views.playlist_details, name="playlist_details"),
  path('mymusic/playlist/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist_delete'),
  path('mymusic/favorite_tracks', views.favorite_tracks, name="favorite_tracks"),
  path('mymusic/favorite_tracks/', views.favorite_tracks, name="favorite_tracks"),
  # path('mymusic/create', views.create, name="create"),
  # path('mymusic/<int:song_id>/', views.detail, name='details'),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
]
