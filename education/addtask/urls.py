from django.urls import path
from .import views as askviews



urlpatterns=[
#add task
path('taskdetails/',askviews.taskdetails,name='taskdetails'),
#done
path('mark_as_done/<int:pk>/',askviews.mark_as_done,name='mark_as_done'),
#undone
path('mark_as_undone/<int:pk>/',askviews.mark_as_undone,name='mark_as_undone'),

#edit
path('mark_as_edit/<int:pk>/',askviews.mark_as_edit,name='mark_as_edit'),

#delete
path('delete_task/<int:pk>/',askviews.delete_task,name="delete_task")

]
