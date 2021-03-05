from django.shortcuts import render
from django.http import HttpResponse
import calendar
import datetime
from datetime import date 
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    if now == 25:
        print('Hurry, it is pay day')
    else:
        print('Sorry, your pay will come 25th')
    title = {'payday':now}

   
    return render(request, 'html/pay.html', title)

#