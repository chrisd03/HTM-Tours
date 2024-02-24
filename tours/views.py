from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class TouristViewSet(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer

class TourGuideViewSet(viewsets.ModelViewSet):
    queryset = Tour_Guide.objects.all()
    serializer_class = TourGuideSerializer