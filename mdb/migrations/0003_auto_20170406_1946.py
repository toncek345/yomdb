# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb', '0002_auto_20170406_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_text',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]