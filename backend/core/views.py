from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page!!!')


def about(request):
    return HttpResponse('About page!!!')
