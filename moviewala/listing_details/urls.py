
from django.urls import path
from . import views

urlpatterns = [
    path('hindi', views.hindi),
    path('movie/', views.movie_method),


]
