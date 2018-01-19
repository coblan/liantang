# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-19 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import helpers.base.jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('liantang', '0004_auto_20180118_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jianfanginfo',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='\u7533\u8bf7\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='jianfanginfo',
            name='shenqing',
            field=helpers.base.jsonfield.JsonField(blank=True, default={}, verbose_name='\u7533\u8bf7\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='jianfanginfo',
            name='xieyi',
            field=helpers.base.jsonfield.JsonField(blank=True, default={}, verbose_name='\u534f\u8bae'),
        ),
    ]
