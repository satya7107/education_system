from django.urls import path
from .import views as chnviews

urlpatterns = [
    path('<int:pk>/',chnviews.chanc_experties,name='chanc_experties')
    ]

