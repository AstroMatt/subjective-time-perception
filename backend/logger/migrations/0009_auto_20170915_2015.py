# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0008_httprequest_data_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='httprequest',
            old_name='datetime',
            new_name='added',
        ),
    ]
