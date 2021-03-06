# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0009_auto_20171130_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_words', models.CharField(blank=True, max_length=255, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('alias', models.SlugField(unique=True)),
                ('short_description', models.TextField()),
                ('body', models.TextField(blank=True, null=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('main_image', models.FileField(upload_to='ministries')),
                ('responsible_person', models.CharField(max_length=255)),
                ('person_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Служение',
                'verbose_name_plural': 'Служения',
            },
        ),
    ]
