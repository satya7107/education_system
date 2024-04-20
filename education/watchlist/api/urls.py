from django.urls import path,include
from watchlist.api import views as wviews


urlpatterns = [
    path('',wviews.allmovies,name='allmovies'),
    path('<int:pk>/',wviews.movielist,name='movielist'),
    ]