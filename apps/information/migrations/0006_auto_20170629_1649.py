# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-29 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20170629_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wincase',
            name='show_index',
            field=models.IntegerField(choices=[(1, '\u9996\u9875\u5c55\u793a'), (0, '\u9996\u9875\u4e0d\u5c55\u793a')], default=0, verbose_name='\u662f\u5426\u9996\u9875\u5c55\u793a'),
        ),
    ]