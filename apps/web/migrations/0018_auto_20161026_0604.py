# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 06:04


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20160921_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='layup_sentiment',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='quality_sentiment',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='sentiment_labeler',
            field=models.CharField(blank=True, choices=[('Manual', 'Sentiment manually recorded'), ('Classifier', 'Sentiment based on classifier')], db_index=True, default=None, max_length=64, null=True),
        ),
    ]
