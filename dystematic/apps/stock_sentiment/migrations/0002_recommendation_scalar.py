# Generated by Django 3.0.6 on 2020-05-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_sentiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='scalar',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]