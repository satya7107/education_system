from django.http import HttpResponse
from django.shortcuts import get_object_or_404 ,render
from mysite .models import student
# Create your views here.
def student_details(request,pk):
    student_obj=get_object_or_404(student,pk=pk)
    dataf={
        'student':student_obj
    }
    return render (request,'student_details.html', dataf)
