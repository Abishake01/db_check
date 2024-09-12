from django.shortcuts import render
from django import *
from .models  import person_coll
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>App is running...</h1>')

 