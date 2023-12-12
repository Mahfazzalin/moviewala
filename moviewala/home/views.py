from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def django(request):
    return HttpResponse('welcome to MovieWala')


def home_page(request):
    return HttpResponse('Home Page')
