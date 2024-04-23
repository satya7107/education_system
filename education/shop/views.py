from django.shortcuts import render
from django.http import HttpResponse
from .models import products,scontact,sorder,order_update
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
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


def scont(request):
    thank=False
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contobj=scontact(name=name,email=email,phone=phone,desc=desc)
        contobj.save()
        thank=True
    return render(request,'scont.html',{'thank':thank})


def stracker(request):
    if request.method=='POST':
        orderId=request.POST.get('orderId')
        email=request.POST.get('email')
        
        try:
            order=sorder.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=order_update.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                    response=json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}') 
        except Exception as e:
            return HttpResponse('{}')

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
    if request.method == "POST":
        items_json=request.POST.get('itemJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + " " + request.POST.get('address2','')
        Zip_code=request.POST.get('Zip_code')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        phone=request.POST.get('phone','')
        oborder=sorder(items_json=items_json,name=name,amount=amount,email=email,address=address,Zip_code=Zip_code,state=state,city=city,phone=phone)
        oborder.save()
        updateobj=order_update(order_id=oborder.order_id, update_desc="Your order has been placed")
        updateobj.save()
        thank=True
        mid=oborder.order_id
        return render(request, 'scheckout.html',{'thank':thank ,'mid':mid})
    return render(request, 'scheckout.html')
@csrf_exempt
def handlerequest(request):
    return HttpResponse("handelrequest")

def sbase(request):
    return render(request, 'sbase.html')