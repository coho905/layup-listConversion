# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 09:17


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20160304_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='confirmation_link',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
