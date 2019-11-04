# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('foo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]