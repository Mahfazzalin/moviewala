from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

def home_page(request):

    return render(request, 'home/home.html')


def bk(request):

    return render(request, 'home/bkash/bkash.html')


def add(request):

    return render(request, 'home/common/base.html')
