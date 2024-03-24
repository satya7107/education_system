from django.urls import path

from .import views as bviews
urlpatterns =[
    path('',bviews.blogindex,name='blogindex'),

]