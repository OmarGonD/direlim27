# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-22 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20170621_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
