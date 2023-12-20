from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('bkash/', views.bk, name='bkash'),
    path('math/', views.add),
    path('movie_request/', views.movie_request)
]
