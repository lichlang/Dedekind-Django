# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sua', '0024_auto_20171028_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsuapublicity',
            name='published_begin_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 23, 55, 34, 902764), verbose_name='开始公示时间'),
        ),
    ]
