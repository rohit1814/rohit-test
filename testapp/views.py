from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def date_time_view(request):
    date = datetime.datetime.now()
    s = '<h1>Current date and time is</h1>' + str(date) +'\n'
    return HttpResponse(s)

