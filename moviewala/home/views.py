from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_page(request):
    return HttpResponse('<h1>Home Page</h1>')


def bkash(request):
    return HttpResponse('payments using Bkash')
