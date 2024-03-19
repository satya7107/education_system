from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import employee,student,user,all_experties,all_experties_ceo,all_experties_chanc,all_experties_prince,all_experties_vice,all_experties_fact
from .models import main_register
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
     if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            ob=main_register.objects.get(username=username,password=password)
            request.session["username"]=ob.username
            request.session["password"]=ob.password
            request.session["rollname"]=ob.rollname
            if ob.rollname=="user":
                return render(request,'home.html',{'user': ob})
            elif ob.rollname=="student":
                details= main_register.objects.all()
                return render(request,'home.html',{"data":details,'user':ob})
            elif ob.rollname == "faculty":
                odetails=main_register.objects.all()
                return render(request,'home.html',{"data1":odetails,'faculty':ob})
        except Exception as e:
            return render(request,'login.html',{'data':"invalid"+str(e)})
        return render(request,'login.html')

def signup(request):
     if request.method ==  "POST":
          username=request.POST['username']
          email=request.POST['email']
          contact=request.POST['contact']
          roll_name=request.POST['roll_name']
          password=request.POST['password']
          image=request.POST['image']
          reg_obj=main_register.objects.create(username=username,email=email,contact=contact,rollname=roll_name,password=password,image=image)
          reg_obj.save();
          return render(request,'signup.html',{'output':"register successfull/login"})

     return render(request,'signup.html')

