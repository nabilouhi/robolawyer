from django.shortcuts import render
from django.views.generic import TemplateView
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
from .dataPreparation.prepareResult import PrepareResult
import json
from django.conf import settings
from django.core.mail import send_mail
# from .forms import FeedbackForm
# Create your views here.


class FormPageView(TemplateView):
    template_name = "applicationForm/form.html"


def formProcessing(request):
    if request.method == 'POST':
        form_dict = request.POST
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


def submittedForm(request):
    if request.method == 'POST':
        print("post value")
        form_dict = request.POST
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = "inline"
        filename = "generated.pdf"
        print(form_dict)
        html = render_to_string('result.html',  {
            'form_data': form_dict})
        font_config = FontConfiguration()
        css = CSS("./static/applicationForm/css/pdf_form.css")
        HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
            response, font_config=font_config, stylesheets=[css, "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"])

        return response


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
