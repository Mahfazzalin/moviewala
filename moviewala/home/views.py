from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

def home_page(request):
    d = datetime.now()
    dt = {'dt': d, 'welcome': 'Welcome to MovieWala. Enjoy your moment.'}
    return render(request, 'home/home.html', context=dt)


def bk(request):

    return render(request, 'home/bkash/bkash.html')


def add(request):

    return render(request, 'home/common/base.html')
