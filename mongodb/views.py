from django.shortcuts import render
from django import *
from .models  import person_coll
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>App is running...</h1>')

def add_person(request):
    records={
        'f_n':'abi',
        'l_n':'mike'
    }
    person_coll.insert_one(records)
    return HttpResponse('New Person is added')

def get_all_person(request):
    persons=person_coll.find()
    return HttpResponse(persons)