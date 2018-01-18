# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-18 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import helpers.base.jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('liantang', '0003_jianfanginfo_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jianfanginfo',
            name='cunwei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liantang.CunWei', verbose_name='\u6751\u59d4'),
        ),
        migrations.AlterField(
            model_name='jianfanginfo',
            name='shenqing',
            field=helpers.base.jsonfield.JsonField(default={}, verbose_name='\u7533\u8bf7\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='jianfanginfo',
            name='state',
            field=models.IntegerField(blank=True, choices=[(1, '\u9547\u89c4\u4fdd\u529e\u521d\u5ba1'), (2, '\u8054\u5e2d\u4f1a\u8bae\u5ba1\u6838'), (3, '\u8054\u5408\u5ba1\u6279(\u89c4\u4fdd\u529e)'), (4, '\u8054\u5408\u5ba1\u6279(\u89c4\u571f\u6240)')], null=True, verbose_name='\u5f53\u524d\u6d41\u7a0b'),
        ),
        migrations.AlterField(
            model_name='jianfanginfo',
            name='xieyi',
            field=helpers.base.jsonfield.JsonField(default={}, verbose_name='\u534f\u8bae'),
        ),
    ]
