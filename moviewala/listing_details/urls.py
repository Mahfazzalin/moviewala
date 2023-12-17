
from django.urls import path
from . import views

urlpatterns = [
    path('hindi', views.hindi),
    path('movies/', views.movie_method, name='moviedata'),


]
