from rest_framework import serializers

from .models import Company, Price, Recommendation


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['symbol', 'shortName', 'sector', 'address1', 'city', 'state', 'country', 'zip']


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['date', 'open', 'high', 'low', 'close', 'volume']


class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    month = serializers.DateField()
    buy = serializers.IntegerField()
    neutral = serializers.IntegerField()
    strong_buy = serializers.IntegerField()
    sell = serializers.IntegerField()
    strong_sell = serializers.IntegerField()
    positive = serializers.IntegerField()
    negative = serializers.IntegerField()

    class Meta:
        model = Recommendation
        fields = ['month', 'buy', 'neutral', 'strong_buy', 'sell', 'strong_sell', 'positive', 'negative']
