from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from todo_app .models import todo_details 
# Create your views here.
def taskdetails(request):
    task1=request.POST['task_details']
    todo_details.objects.create(task=task1)
    return redirect('todo_app')

def mark_as_done(request,pk) :
    task_obj=get_object_or_404(todo_details,pk=pk)
    task_obj.is_complete=True
    task_obj.save()
    return redirect('todo_app')

def mark_as_undone(request,pk):
    task_obj1=get_object_or_404(todo_details,pk=pk)
    task_obj1.is_complete=False
    task_obj1.save()
    return redirect('todo_app')

def mark_as_edit(request,pk):
    get_task=get_object_or_404(todo_details,pk=pk)
    if request.method == 'POST':
        task2=request.POST['task_details']
        get_task.task=task2
        get_task.save()
        return redirect('todo_app')
    else:
        get_task_data={
            'get_task':get_task
        }
        return render(request,'edit_task.html',get_task_data)
    
def delete_task(request,pk):
    del_task=get_object_or_404(todo_details,pk=pk)
    del_task.is_complete=True
    del_task.delete()
    return redirect('todo_app')


