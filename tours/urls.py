from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tourists', TouristViewSet, basename='tourists')
router.register(r'tour_guides', TourGuideViewSet, basename='tour guides')
router.register(r'acceptances', AcceptancesViewSet, basename='acceptances')

urlpatterns = [
    path('', include(router.urls)),
]