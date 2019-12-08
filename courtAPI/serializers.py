from rest_framework import serializers
from .models import CourtDetail


class CourtCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourtDetail
        fields = ('country', 'proceedingType1', 'court1',
                  'proceedingType2', 'court2', 'proceedingType3', 'court3',)
