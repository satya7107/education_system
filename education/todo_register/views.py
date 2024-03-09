from django.shortcuts import render
from django.http import HttpResponse
from .models import todoregisternew
# Create your views here.

def dsignup(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        rolname=request.POST['rolname']
        regobj=todoregisternew.objects.create(username=name,email=email,password=password,rol_name=rolname)
        regobj.save()
        return render(request,'dsignup.html',{'output':"register successful"})


    return render (request,'dsignup.html')


