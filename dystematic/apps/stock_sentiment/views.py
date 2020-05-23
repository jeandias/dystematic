from rest_framework import viewsets

from .models import Company, Price, Recommendation
from .serializers import CompanySerializer, PriceSerializer, RecommendationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('symbol')
    serializer_class = CompanySerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('-date')
    serializer_class = PriceSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all().order_by('-date')
    serializer_class = RecommendationSerializer
