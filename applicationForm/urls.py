from django.urls import path, include
from .views import FormPageView, submittedForm, formProcessing

urlpatterns = [
    path('', FormPageView.as_view(), name='form'),
    # path('formSubmit', submittedForm, name='formSubmit'),
    path('submit', formProcessing, name='formProcessing')
    # path('generate/', generatePDF, name='generate')
    # path('', form, name='form'),
    # path('/formSubmit', formSubmit, name='formSubmit'),
]
