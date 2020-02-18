from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
from .dataPreparation.prepareResult import PrepareResult
import json
from django.conf import settings
from django.core.mail import send_mail


class FormPageView(TemplateView):
    template_name = "applicationForm/form.html"


def formProcessing(request):
    if request.method == 'POST':
        form_dict = request.POST
        print(form_dict)
        pagesName = ['page1', 'page2', 'page3', 'page4', 'page5',
                     'page6', 'page7', 'page8', 'page9', 'page10']
        pages = []
        for page in pagesName:
            pages.append(dict((key, value) for (
                key, value) in form_dict.items() if page in key.lower()))
        for page in pages:
            print(page)
            prepareResult = PrepareResult(pages)
            prepareResult.main()    
    return HttpResponse("it's working")


def feedback(request):
    if request.method == 'POST':
        pageNo = request.POST.get('pageNo')
        legalTrained = request.POST.get('legalExp')
        suggestion = request.POST.get('suggestion')
        print(suggestion)
        subject = "suggestionEmail"
        message = "1. Page No. - " + str(pageNo) + "\n2. Legal Trained - " + \
            str(legalTrained) + "\n3. Suggestion - " + str(suggestion)
        from_user = settings.EMAIL_HOST_USER
        to = ["contact@justbot.org"]
        send_mail(subject, message, from_user, to, fail_silently=False)

    return HttpResponse('We have received your feedback.')
