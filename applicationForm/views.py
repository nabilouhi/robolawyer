from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponse, FileResponse, Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from .dataPreparation.prepareResult import PrepareResult
import json
from django.conf import settings
from django.core.mail import send_mail
import os
import logging
logger = logging.getLogger(__name__)

class FormPageView(TemplateView):
    template_name = "applicationForm/form.html"


def formProcessing(request):
    import uuid
    sessionID = uuid.uuid4().hex
    spclReplies = []
    filepath = os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/results/'+sessionID+'/finalPage/finalForm.pdf')
    if request.method == 'POST':
        form_dict = request.POST
        spclReplies.append(request.POST.getlist('page1[involvedStates]'))

        spclReplies.append(request.POST.getlist('page5[articleSelect]'))
        spclReplies.append(request.POST.getlist('page5[articleExplanation]'))
        
        spclReplies.append(request.POST.getlist('page6[complainSelect]'))
        spclReplies.append(request.POST.getlist('page6[complaintDate]'))
        spclReplies.append(request.POST.getlist('page6[remediesUsed]'))

        spclReplies.append(request.POST.getlist('page8[finalDecisionDate]'))
        spclReplies.append(request.POST.getlist('page8[docTitle]'))
        spclReplies.append(request.POST.getlist('page8[docDescription]'))
        spclReplies.append(request.POST.getlist('page8[pageNumber]'))

       
        pagesName = ['page1', 'page2', 'page3', 'page4', 'page5',
                     'page6', 'page7', 'page8', 'page9', 'page10']
        pages = {}
        for page in pagesName:
            pages[page] = dict((key, value) for key, value in form_dict.items() if page in key.lower())

        prepareResult = PrepareResult(pages, sessionID, spclReplies)
        prepareResult.main()  
        logger.warning("Your log message is here")

    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')    
    # return render(request, 'applicationForm/finalPage.html', {'filepath': filepath})


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
    else:
        return HttpResponse('Our developers are working to resolve this issue. Please try after sometime.')

    

# def download(request, path, sessionID):
#     file_path = path
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404


def download(request, path):
    try:
        return FileResponse(open(path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


# def finalView(request):
#     filerequest = download(request, filepath)
#     return render(request, )