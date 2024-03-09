from django.shortcuts import render
from .models import todo_details

# Create your views here.
def todo_app(request):
    todo_obj=todo_details.objects.filter(is_complete=False).order_by('-update_at')
    completed_task_obj=todo_details.objects.filter(is_complete=True)
    
    todo_data={
        'todoall':todo_obj,
        'completed_task':completed_task_obj
    }
    return render(request,'to_do.html',todo_data)