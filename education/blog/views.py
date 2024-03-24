from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogindex(request):
    return render(request,"blogindex.html")