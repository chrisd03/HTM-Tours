from rest_framework import serializers
from .models import *

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

class TourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour_Guide
        fields = '__all__'

class AcceptancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceptances
        fields = '__all__'
