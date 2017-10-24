# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v3', '0006_auto_20171003_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='is_valid',
        ),
        migrations.AlterField(
            model_name='result',
            name='request_sha1',
            field=models.CharField(db_index=True, max_length=40, unique=True, verbose_name='HTTP Request SHA1'),
        ),
    ]