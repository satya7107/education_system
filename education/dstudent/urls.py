from django.urls import path
from .import views as aoviews



urlpatterns = [
    path('<int:pk>/',aoviews.student_details,name='student_details')
]