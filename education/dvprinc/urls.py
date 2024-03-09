from django.urls import path
from .import views as vpriviews 

urlpatterns = [
    path('<int:pk>/',vpriviews.vprinc_experties,name='vprinc_experties')
]