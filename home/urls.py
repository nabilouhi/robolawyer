from django.urls import path
from .views import home, testing

urlpatterns = [
    path('', home, name='home'),
    path('testing', testing, name="testing")
]
