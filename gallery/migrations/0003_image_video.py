# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180109_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='video',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
