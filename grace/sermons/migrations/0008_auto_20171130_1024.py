# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0007_auto_20171130_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblebook',
            name='part_of_bible',
            field=models.CharField(choices=[('nt', 'Новый Завет'), ('ot', 'Ветхий Завет')], default='nt', max_length=2),
        ),
    ]
