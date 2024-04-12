from django.urls import path
from .import views as sviews

urlpatterns = [
            path('',sviews.shopindex,name='shopindex'),
            path('sabout/',sviews.sabout,name='sabout'),
            path('scont/',sviews.scont,name='scont'),
            path('stracker/',sviews.stracker,name='stracker'),
            path('ssearch/',sviews.ssearch,name='ssearch'),
            path('sproductview/<int:myid>/',sviews.sproductview,name='sproductview'),
            path('scheckout/',sviews.scheckout,name='scheckout'),
            path('sbase',sviews.sbase),
]