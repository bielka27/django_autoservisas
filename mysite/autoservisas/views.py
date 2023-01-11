from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Sveiki atvykę į automobilių servisą!")


# Create your views here.
