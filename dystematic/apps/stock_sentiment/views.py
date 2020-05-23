from rest_framework import viewsets
from rest_framework import generics

from .models import Company, Price, Recommendation
from .serializers import CompanySerializer, PriceSerializer, RecommendationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('symbol')
    serializer_class = CompanySerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all().order_by('-date')
    serializer_class = RecommendationSerializer


class PriceList(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        qs = Price.objects.filter()

        ticker = self.request.GET.get('ticker', False)
        if ticker:
            qs = qs.filter(company__symbol=ticker)

        start_date = self.request.GET.get('start_date', False)
        end_date = self.request.GET.get('end_date', False)
        if start_date and end_date:
            qs = qs.filter(date__range=(start_date, end_date))

        return qs
