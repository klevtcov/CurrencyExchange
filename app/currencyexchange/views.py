from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import requests
from .forms import CurrExch

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return redirect('home')
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'news/register.html', {'form': form})




def exchange(request):
    # form_class = CurrExch
    form = CurrExch()
    # по умолчанию редирект на сам объект, т.к. есть метод get_absolute_url в модели
    # success_url = reverse_lazy('home')
    # template_name = 'currencyexchange/index.html'
    # redirect_field_name = 'redirect_to'
    # raise_exception = True

    response = requests.get(url='https://open.er-api.com/v6/latest/USD').json()
    currencies = response.get('rates')

    if request.method == 'GET':
    
        context = {
            'currencies': currencies,
            'form': form
        }
    
        return render(request, 'currencyexchange/index.html', context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'form': form
        }

        return render(request, 'currencyexchange/index.html', context)





# def exchange(request):
    
#     response = requests.get(url='https://open.er-api.com/v6/latest/USD').json()
#     currencies = response.get('rates')

#     if request.method == 'GET':
    
#         context = {
#             'currencies': currencies
#         }
    
#         return render(request=request, template_name='currencyexchange/index.html', context=context)

#     if request.method == 'POST':
#         from_amount = float(request.POST.get('from_amount'))
#         from_curr = request.POST.get('from_curr')
#         to_curr = request.POST.get('to_curr')

#         converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

#         context = {
#             'currencies': currencies,
#             'converted_amount': converted_amount,
#             'from_curr': from_curr,
#             'to_curr': to_curr
#         }

#         return render(request=request, template_name='currencyexchange/index.html', context=context)