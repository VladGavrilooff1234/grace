# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20171206_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
