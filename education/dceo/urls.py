from django.urls import path
from .import views as cviews

urlpatterns=[
path('<int:pk>/',cviews.ceo_experties,name='ceo_experties'),
]