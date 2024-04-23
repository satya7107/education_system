from django.urls import path

from .import views as bviews
urlpatterns =[
    path("",bviews.blogindex,name='blogindex'),
    path("allblogpost/<int:pk>/",bviews.allblogpost,name='allblogpost'),

]