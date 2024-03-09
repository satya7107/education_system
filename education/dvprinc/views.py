from django.shortcuts import render,get_object_or_404
from mysite .models import all_experties_vice
# Create your views here.
def vprinc_experties(request,pk):
    vprinc_obj=get_object_or_404(all_experties_vice,pk=pk)
    vprinc_data={
        'vprincexperties':vprinc_obj
    }

    return render(request,'vprinc_experties.html',vprinc_data)