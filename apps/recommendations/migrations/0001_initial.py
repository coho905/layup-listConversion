# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-09 03:23


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0016_auto_20160319_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(choices=[('docsim', 'Document Similarity')], max_length=16)),
                ('weight', models.FloatField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='web.Course')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommenders', to='web.Course')),
            ],
        ),
    ]
