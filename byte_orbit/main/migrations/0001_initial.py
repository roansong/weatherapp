# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Forecast date')),
                ('min_temp', models.IntegerField(verbose_name='Min temp')),
                ('max_temp', models.IntegerField(verbose_name='Max temp')),
                ('wind', models.IntegerField(verbose_name='Wind')),
                ('rain', models.IntegerField(verbose_name='Rain')),
            ],
        ),
    ]
