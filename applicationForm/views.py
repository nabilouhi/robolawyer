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


# def feedbackForm(request):
#     form = FeedbackForm()
#     return render(request, 'applicationForm/feedback.html', {'form': form})


# def feedback(request):
#     if request.method=="post":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             legalExp = form.cleaned_data['legalTraining']
#             suggestion = form.cleaned_data['suggestion']
#             return render(request, '')

def feedback(request):
    print(request)
    if request.method == 'POST':
        legalExp = request.POST['legalExp']
        suggestion = request.POST['suggestion']

    return HttpResponse('We have received your feedback.')


# class FeedbackView(BSModalCreateView):
#     template_name = 'applicationForm/feedback.html'
#     form_class = BookForm
#     success_message = 'Success: feedback was created.'
#     success_url = reverse_lazy('')
