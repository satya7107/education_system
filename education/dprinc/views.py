from django.shortcuts import render,get_object_or_404
from mysite .models import all_experties_prince

# Create your views here.
def princ_experties(request,pk):
    princ_obj=get_object_or_404(all_experties_prince,pk=pk)
    princ_data={
        'princexperties':princ_obj
    }

    return render(request,'princ_experties.html',princ_data)