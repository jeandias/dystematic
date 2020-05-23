from celery import shared_task
import yfinance as yf
from .models import Company, Price, Recommendation


@shared_task
def fetch_stock_data():
    tickers = ['FB', 'AAPL', 'NFLX', 'GOOG']

    Company.objects.all().delete()
    for t in tickers:
        ticker = yf.Ticker(t)

        company = Company(
            shortName=ticker.info['shortName'],
            symbol=ticker.info['symbol'],
            sector=ticker.info['sector'],
            address1=ticker.info['address1'],
            city=ticker.info['city'],
            state=ticker.info['state'],
            country=ticker.info['country'],
            zip=ticker.info['zip'],
        )
        company.save()

        prices = yf.download(company.symbol)
        for index, row in prices.iterrows():
            price = Price(
                company=company,
                date=index.date(),
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
            )
            price.save()

        recommendations = ticker.recommendations
        for index, row in recommendations.iterrows():
            recommendation = Recommendation(
                company=company,
                date=index.date(),
                recommendation=row['To Grade'],
                firm=row['Firm'],
            )
            recommendation.save()
