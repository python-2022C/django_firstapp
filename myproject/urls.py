from django.contrib import admin
from django.urls import path
from arithmetics_app import views

urlpatterns = [
    path('', views.home),
    path('subtracts/', views.subtracts),
    path("division/", views.division),
    path("multiple/", views.multiple)
]
