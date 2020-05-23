from rest_framework import viewsets
from rest_framework import generics

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


class PriceList(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        ticker = self.request.GET['ticker']
        start_date = self.request.GET['start_date']
        end_date = self.request.GET['end_date']
        return Price.objects.filter(company__symbol=ticker, date__gte=start_date, date__lte=end_date)
