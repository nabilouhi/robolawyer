from django.shortcuts import render
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from pdfrw import PdfReader
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


# def testing(request):
#     pathToPdf = finders.find('App_form.pdf')
#     pdf = PdfReader(pathToPdf)
#     result = pdf.Root.Pages.Kids
#     return HttpResponse(result)

def testing(request):
    pathToPdf = finders.find('App_form.pdf')
    x = PdfReader(pathToPdf)
    result = x.pages[0]
    return HttpResponse(result)
