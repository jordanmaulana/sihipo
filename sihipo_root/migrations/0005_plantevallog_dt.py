# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sihipo_root', '0004_auto_20171210_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantevallog',
            name='dt',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Waktu'),
        ),
    ]
