from django.urls import path, include
from .views import form, formSubmit

urlpatterns = [
    # path('', FormPageView.as_view(), name='form'),
    # path('finish', submittedForm, name='submitForm'),
    # path('generate/', generatePDF, name='generate')
    path('', form, name='form'),
    path('/formSubmit', formSubmit, name='formSubmit'),
]
