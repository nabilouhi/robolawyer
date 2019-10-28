from django.shortcuts import render
from django.contrib.staticfiles import finders
from django.http import HttpResponse
# Create your views here.


def home(request):
    print("for testing")
    return render(request, 'home/home.html')
