# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 17:05
from __future__ import unicode_literals

import Restaurant.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0005_auto_20161217_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=Restaurant.models.upload_location),
        ),
    ]
