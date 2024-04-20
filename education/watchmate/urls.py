from django.urls import path,include


urlpatterns = [
    path('watchlist/',include('watchlist.api.urls'))
]