# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-10 06:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200110_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 6, 52, 25, 792966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 6, 52, 25, 791930, tzinfo=utc)),
        ),
    ]
