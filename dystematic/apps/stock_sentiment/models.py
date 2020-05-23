from django.db import models


class Company(models.Model):
    shortName = models.CharField(max_length=50, null=False)
    symbol = models.CharField(max_length=10, null=False, unique=True)
    sector = models.CharField(max_length=30, null=False)
    address1 = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=2, null=False)
    country = models.CharField(max_length=30, null=False)
    zip = models.CharField(max_length=10, null=False)


class Price(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    open = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    close = models.FloatField(null=False)
    volume = models.FloatField(null=False)


class Recommendation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    recommendation = models.CharField(max_length=50, null=False)
    firm = models.CharField(max_length=50, null=False)
    scalar = models.FloatField(null=False)
