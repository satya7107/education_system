from django.urls import path
from .import views as abviews



urlpatterns = [
    path('<int:pk>/',abviews.user_details,name='user_details')
]