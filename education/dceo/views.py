from django.shortcuts import render,get_object_or_404
from mysite.models import all_experties_ceo

# Create your views here.
def ceo_experties(request,pk):
    ceo_obj=get_object_or_404(all_experties_ceo,pk=pk)
    ceo_data={
        'ceofiles':ceo_obj
    }
    return render(request,'ceo_experties.html',ceo_data)
