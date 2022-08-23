from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

def exchange(request):
    name = 'Test'
    
    context = {
        'name': name
    }
    
    return render(request=request, template_name='currencyexchange/index.html', context=context)

