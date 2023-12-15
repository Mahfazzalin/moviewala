from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('bkash/', views.bk),
    path('math/', views.add),
]
