from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from .forms import SampleForm  
def newform(request):  
    form = SampleForm(request.POST)  
    return render(request, 'sampleform.html', {'form': form})  
