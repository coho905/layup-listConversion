# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 05:06


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 10, 5, 6, 8, 21139, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 10, 5, 6, 14, 645022, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
