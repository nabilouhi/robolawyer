from django.shortcuts import render

# Create your views here.


def extResPage(request):
    return render(request, 'extResources/extResources.html')
