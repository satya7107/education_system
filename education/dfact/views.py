from django.shortcuts import render,get_object_or_404
from mysite .models import all_experties_fact

# Create your views here.
def fact_experties(request,pk):
    fact_obj=get_object_or_404(all_experties_fact,pk=pk)
    fact_data={
        'factexperties':fact_obj
    } 
    return render(request,'fact_experties.html',fact_data)