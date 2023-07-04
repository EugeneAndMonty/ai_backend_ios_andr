
from django.contrib import admin
from django.urls import path
from django_flutter_app import views

urlpatterns = [
    path('for_test', views.for_test),
    path('for_freinds', views.for_freinds)
]
