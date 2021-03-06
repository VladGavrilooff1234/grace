# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 11:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('part_of_bible', models.CharField(choices=[('nt', 'Новый Завет'), ('ot', 'Ветхий Завет')], default='nt', max_length=2)),
            ],
            options={
                'verbose_name': 'Книга Библии',
                'verbose_name_plural': 'Книги Библии',
            },
        ),
        migrations.CreateModel(
            name='Preacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_member', models.BooleanField()),
                ('photo', models.FileField(upload_to='preachers')),
            ],
            options={
                'verbose_name': 'Проповедник',
                'verbose_name_plural': 'Проповедники',
            },
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('chapter_and_verses', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_chapter_and_verses', message='Место Писания должно быть в формате: 1:1, 1:10-21', regex='^\\d{1,3}:\\d{1,3}-{0,1}\\d{0,3}$')])),
                ('date_of_sermon', models.DateTimeField()),
                ('audio', models.FileField(upload_to='sermons')),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('bible_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sermons.Biblebook')),
                ('preacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sermons.Preacher')),
            ],
            options={
                'verbose_name': 'Проповедник',
                'verbose_name_plural': 'Проповедники',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тема проповеди',
                'verbose_name_plural': 'Темы проповедей',
            },
        ),
        migrations.AddField(
            model_name='sermon',
            name='topics',
            field=models.ManyToManyField(to='sermons.Tag'),
        ),
    ]
