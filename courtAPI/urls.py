from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'courtAPI'
router = routers.DefaultRouter()
router.register(r'', views.CourtViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
