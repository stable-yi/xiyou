# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-27 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20170627_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.VisaType', verbose_name='\u7b7e\u8bc1\u7c7b\u578b'),
        ),
    ]
