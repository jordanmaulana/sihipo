# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 08:35
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sihipo_root', '0009_auto_20180128_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantbase',
            name='note',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Catatan'),
        ),
    ]