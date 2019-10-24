

from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


class FormPageView(TemplateView):
    template_name = "applicationForm/form.html"


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
