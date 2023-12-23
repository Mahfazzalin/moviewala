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
    if request.method == 'POST':
        frm = MovieRequest(request.POST)
        if frm.is_valid():
            print('valid form')
            print(frm.cleaned_data)
    
    else:
        frm = MovieRequest(auto_id=True, label_suffix=' :')
        print('get statement')

    # frm.order_fields(field_order=['From', 'To', 'subject', 'Moviename'])
    return render(request, 'home/MovieRequestForm.html', {'form': frm})
