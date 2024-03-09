from django.urls import path
from .import views as princviews

urlpatterns =[
    path('<int:pk>/',princviews.princ_experties,name='princ_experties')
]