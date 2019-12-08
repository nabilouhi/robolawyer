from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EchrCountrySerializer
from .models import EchrDetail
import csv


# @api_view(['GET'])
# def Echr_detail_view(request):
#     try:
#         echr_detail = EchrDetail.get()
#     except:
#         EchrDetail.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EchrCountrySerializer(echr_detail)
#         return Response(serializer.data)


class EchrViewSet(viewsets.ModelViewSet):
    queryset = EchrDetail.objects.all().order_by('country')
    serializer_class = EchrCountrySerializer

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
