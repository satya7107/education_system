from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import employee,student,user,all_experties,all_experties_ceo,all_experties_chanc,all_experties_prince,all_experties_vice,all_experties_fact

# Create your views here.

def index1(request):
    return HttpResponse ('<p>hello</p>')
def index(request):
    obj=employee.objects.all()
    obj1=student.objects.all()
    obj2=user.objects.all()
    data={
        'employees':obj,
        'student':obj1,
        'user':obj2
    }
 
    return render(request,'index.html',data)


def header (request):
    return render(request,'header.html')
def footer (request):
    return render(request,'footer.html')
def base (request):
    return render(request,'base.html')
def homepage (request):
    return render(request,'homepage.html')
def features (request):
    return render(request,'features.html')

def experties(request):
    obj=all_experties.objects.all()
    obj1=all_experties_ceo.objects.all()
    obj2=all_experties_chanc.objects.all()
    obj3=all_experties_prince.objects.all()
    obj4=all_experties_vice.objects.all()
    obj5=all_experties_fact.objects.all()    
    data={
         'all_experties':obj,
         'experties_ceo':obj1,
         'experties_chance':obj2,
         'experties_prince':obj3,
         'experties_vice':obj4,
         'experties_fact':obj5
    }
    
    return render(request,'experties.html',data)

def contactus(request):
	return render(request,'contactus.html')

def gallery(request):
     return render(request,'gallery.html') 

def login(request):
     return render(request,'login.html')

def signup(request):
     return render(request,'signup.html')

