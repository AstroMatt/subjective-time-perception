# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0012_auto_20170928_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httprequest',
            name='api_version',
            field=models.PositiveSmallIntegerField(default=3, verbose_name='API version'),
        ),
        migrations.AlterField(
            model_name='httprequest',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='httprequest',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PATCH', 'PATCH'), ('PUT', 'PUT'), ('HEAD', 'HEAD')], default='POST', max_length=10, verbose_name='Method'),
        ),
    ]
