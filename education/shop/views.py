from django.shortcuts import render
from django.http import HttpResponse
from .models import products
from math import ceil
# Create your views here.

def shopindex(requet):
    # # prodobj=products.objects.all()
    # n=len(prodobj)
    # nSlides=n//4 +ceil((n/4)+(n//4) )
    allprods=[]
    catprods=products.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=products.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 +ceil((n/4)+(n//4) )
        allprods.append([prod,range(1,nSlides),nSlides])

    
    # allprods=[[prodobj,range(1,nSlides),nSlides],
    #           [prodobj,range(1,nSlides),nSlides]]
    # context={
    #     'products':prodobj,
    #     'no_of_slides':nSlides,
    #     'range':range(1,nSlides),
    # }
    context={
        "allprods":allprods
    }
    return render(requet, 'shopindex.html',context)

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
