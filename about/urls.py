from django.urls import path, include
from .views import aboutPage

urlpatterns = [
    path('', aboutPage, name='about'),
]
