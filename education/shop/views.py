from django.shortcuts import render
from django.http import HttpResponse
from .models import products,scontact
from math import ceil
# Create your views here.

def shopindex(request):
    # # prodobj=products.objects.all()
    # n=len(prodobj)
    # nSlides=n//4 +ceil((n/4)+(n//4) )
    allprods=[]
    catprods=products.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=products.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 +ceil((n/4)-(n//4) )
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
    return render(request, 'shopindex.html',context)

def sabout(request):
    return render(request, 'sabout.html')

def scontact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contobj=scontact(name=name,email=email,phone=phone,desc=desc)
        contobj.save()
    return render(request,'scontact.html')

def stracker(request):
    return render(request, 'stracker.html')

def ssearch(request):
    return render(request, 'ssearch.html')

def sproductview(request,myid):
    all_products=products.objects.filter(id=myid)
    context={
        "myproducts": all_products[0]
    }
    return render(request, 'sproductview.html',context)

def scheckout(request):
    return render(request, 'scheckout.html')

def sbase(request):
    return render(request, 'sbase.html')