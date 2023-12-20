from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.forms import MovieRequest


# Create your views here.

def home_page(request):
    return render(request, 'home/home.html')


def bk(request):
    return render(request, 'home/bkash/bkash.html')


def add(request):
    return render(request, 'home/common/base.html')


def movie_request(request):
    frm = MovieRequest()
    return render(request, 'home/MovieRequestForm.html', {'form': frm})

