# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180329_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadSubmergenceDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('date_discharge', models.DecimalField(decimal_places=10, max_digits=20)),
                ('road_submergence', models.CharField(max_length=10)),
            ],
        ),
    ]