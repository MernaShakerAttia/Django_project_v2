# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0002_admin_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_reply', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_reply',
        ),
        migrations.AddField(
            model_name='reply',
            name='post_reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeks.Post'),
        ),
    ]