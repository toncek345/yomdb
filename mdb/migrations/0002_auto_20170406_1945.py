# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_text',
            field=models.CharField(max_length=200),
        ),
    ]