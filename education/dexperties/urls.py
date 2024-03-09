from django.urls import path
from .import views as expviews


urlpatterns = [
    path('<int:pk>/',expviews.chair_experties,name="chair_experties"),
    
]