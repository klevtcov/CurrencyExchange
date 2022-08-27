from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import requests

# Create your views here.




def exchange(request):
    
    response = requests.get(url='https://open.er-api.com/v6/latest/USD').json()
    currencies = response.get('rates')
   
    if request.method == 'GET':
    
        context = {
            'currencies': currencies
        }
    
        return render(request=request, template_name='currencyexchange/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
            'from_curr': from_curr,
            'to_curr': to_curr
        }

        return render(request=request, template_name='currencyexchange/index.html', context=context)