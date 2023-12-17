from django.shortcuts import render
from django.http import HttpResponse
from listing_details.models import movie_details


# Create your views here.


def hindi(request):
    return HttpResponse('here will show all the hindi movie')


def movie_method(request):
    mov_method = movie_details.object.all()
    return render(request, 'listing_details/list.html', {'movie': mov_method})
