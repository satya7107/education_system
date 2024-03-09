from django.shortcuts import render,get_object_or_404,render
from mysite.models import all_experties_chanc

# Create your views here.
def chanc_experties(request,pk):
    chanc_obj=get_object_or_404(all_experties_chanc,pk=pk)
    chanc_data={
        'chancexperties':chanc_obj,
    }
    return render(request,'chanc_experties.html',chanc_data)