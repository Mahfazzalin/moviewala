from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_page(request):
    return HttpResponse('<h1>Home Page</h1>')


def bk(request):
    return HttpResponse('payments using Bkash')


def add(request):
    z = 123456678900*345678
    print(z)
    return HttpResponse(z)
