from django.urls import path, include
from .views import FormPageView, formProcessing, feedback

urlpatterns = [
    path('', FormPageView.as_view(), name='form'),
    path('submit', formProcessing, name='formProcessing'),
    path('feedback', feedback, name="feedback")
]
