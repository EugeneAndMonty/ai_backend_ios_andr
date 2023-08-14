
from django.contrib import admin
from django.urls import path
from backend_app import views

urlpatterns = [
    path('for_test', views.for_test),
    path('', views.hello)
]
