from rest_framework import serializers
from .models import EchrDetail


class EchrCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EchrDetail
        fields = ('country', 'ratDate')
