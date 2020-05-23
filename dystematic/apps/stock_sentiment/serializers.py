from rest_framework import serializers

from .models import Company, Price, Recommendation


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['symbol', 'shortName', 'sector', 'address1', 'city', 'state', 'country', 'zip']


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['company', 'date', 'open', 'high', 'low', 'close', 'volume']


class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['company', 'date', 'recommendation', 'scalar', 'firm']
