# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-10 06:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200110_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 6, 5, 5, 413332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 6, 5, 5, 412298, tzinfo=utc)),
        ),
    ]
