from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request,data):
    return HttpResponse(f'<h1>you entered {data}</h1>')