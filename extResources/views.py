from django.shortcuts import render
from django.contrib.staticfiles import finders

# Create your views here.


def extResPage(request):
    return render(request, 'extResources/extResources.html')
