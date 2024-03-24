from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shopindex(requet):
    return render(requet, 'shopindex.html')

def about(requet):
    return HttpResponse("iam about")

def contact(requet):
    return HttpResponse("iam contact")

def tracker(requet):
    return HttpResponse("iam tracker")

def search(requet):
    return HttpResponse("iam search")

def productview(requet):
    return HttpResponse("iam productview")

def checkout(requet):
    return HttpResponse("iam checkout")
