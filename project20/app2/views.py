from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>httpresponse of apps2</h1>')

def sample(request):
    return render(request,'sample2.html')

