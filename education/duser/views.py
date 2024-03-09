from django.shortcuts import render ,get_object_or_404
from mysite .models import user
from django.http import HttpResponse

# Create your views here.

def user_details(request,pk):
    user_obj=get_object_or_404(user,pk=pk)
    data1={
        'user1':user_obj
    }
    return  render(request,'user_details.html',data1)
    
