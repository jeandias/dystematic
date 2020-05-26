from django.db.models import Func, F, Q, Value, Count
from rest_framework import viewsets
from rest_framework import generics

from .models import Company, Price, Recommendation
from .serializers import CompanySerializer, PriceSerializer, RecommendationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('symbol')
    serializer_class = CompanySerializer


class PriceList(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        qs = Price.objects.all()

        ticker = self.request.GET.get('ticker', False)
        if ticker:
            qs = qs.filter(company__symbol=ticker)

        start_date = self.request.GET.get('start_date', False)
        end_date = self.request.GET.get('end_date', False)
        if start_date and end_date:
            qs = qs.filter(date__range=(start_date, end_date))

        return qs


class RecommendationList(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        qs = Recommendation.objects.all()

        ticker = self.request.GET.get('ticker', False)
        if ticker:
            qs = qs.filter(company__symbol=ticker)

        start_date = self.request.GET.get('start_date', False)
        end_date = self.request.GET.get('end_date', False)
        if start_date and end_date:
            qs = qs.filter(date__range=(start_date, end_date))

        return qs.annotate(month=Func(F('date'), Value('YYYY-MM'), function='TO_CHAR')).values('month').annotate(
            buy=Count('recommendation', filter=Q(recommendation='Buy')),
            neutral=Count('recommendation', filter=Q(recommendation='Neutral')),
            strong_buy=Count('recommendation', filter=Q(recommendation='Strong Buy')),
            sell=Count('recommendation', filter=Q(recommendation='Sell')),
            strong_sell=Count('recommendation', filter=Q(recommendation='Strong Sell')),
            positive=Count('recommendation', filter=Q(recommendation='Positive')),
            negative=Count('recommendation', filter=Q(recommendation='Negative'))).order_by(
            Func(F('date'), Value('YYYY-MM'), function='TO_CHAR')).values(
            'month', 'buy', 'neutral', 'strong_buy', 'sell', 'strong_sell', 'positive', 'negative')
