from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
from django.shortcuts import get_object_or_404

# Create your views here.
def blogindex(request):
    mypost=blogpost.objects.all()
    context={
       'mypost':mypost
    }
    return render(request,"blogindex.html",context)

def allblogpost(request,pk):
    blogobj=get_object_or_404(blogpost,pk=pk)
    context={
        'post':blogobj
    }
    return render(request,"allblogpost.html",context)    