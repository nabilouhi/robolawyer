from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CourtCountrySerializer
from .models import CourtDetail


class CourtViewSet(viewsets.ModelViewSet):
    queryset = CourtDetail.objects.all().order_by('country')
    serializer_class = CourtCountrySerializer

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
