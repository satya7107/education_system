from django.shortcuts import get_object_or_404, render
from mysite.models import all_experties
# Create your views here.
def chair_experties(request,pk):
    expert_obj1=get_object_or_404(all_experties,pk=pk)
    
    ex_data={
            'all_chair':expert_obj1,
            
    }
    return render(request,'chair_experties.html',ex_data)