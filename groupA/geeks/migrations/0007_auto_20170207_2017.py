# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0006_auto_20170207_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 7, 20, 17, 57, 157304)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 7, 20, 17, 57, 156629)),
        ),
    ]
