# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-18 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liantang', '0002_auto_20180118_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='jianfanginfo',
            name='phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
    ]
