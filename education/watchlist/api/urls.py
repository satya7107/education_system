from django.urls import path,include
# from watchlist.api import views as wviews
from watchlist.api.views import allmovies,movielist


urlpatterns = [
    path('',allmovies.as_view(),name='allmovies'),
    path('<int:pk>/',movielist.as_view(),name='movielist'),



    # path('',wviews.allmovies,name='allmovies'),
    # path('<int:pk>/',wviews.movielist,name='movielist'),
    ]