# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180111_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='V',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]