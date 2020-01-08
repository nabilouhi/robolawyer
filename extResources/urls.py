from django.urls import path, include
from .views import extResPage

urlpatterns = [
    path('', extResPage, name='extResPage')
]
