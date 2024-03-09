from django.urls import path
from .import  views as factview

urlpatterns=[
    path('<int:pk>/',factview.fact_experties,name='fact_experties')
]