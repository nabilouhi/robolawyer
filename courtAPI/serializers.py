from rest_framework import serializers
from .models import CourtDetail


class CourtCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourtDetail
        fields = ('country', 'proceedingType', 'court')
