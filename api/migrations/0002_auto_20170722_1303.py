# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='date',
            field=models.DateField(unique=True, verbose_name='Forecast date'),
        ),
    ]