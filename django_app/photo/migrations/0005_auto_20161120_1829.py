# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20161120_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('-pk',)},
        ),
        migrations.AddField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
