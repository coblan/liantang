# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-29 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liantang', '0013_auto_20180329_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jianfanginfo',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, '-----'), (11, '\u6751\u59d4\u4f1a\u9884\u5ba1'), (1, '\u9547\u89c4\u4fdd\u529e\u521d\u5ba1'), (2, '\u8054\u5e2d\u4f1a\u8bae\u5ba1\u6838'), (3, '\u8054\u5408\u5ba1\u6279(\u89c4\u4fdd\u529e)'), (4, '\u8054\u5408\u5ba1\u6279(\u89c4\u571f\u6240)'), (5, '\u8054\u5408\u5ba1\u6279(\u9547\u653f\u5e9c)'), (6, '\u8054\u5408\u5ba1\u6279(\u533a\u89c4\u571f\u6240)'), (7, '\u9547\u6751\u516c\u793a'), (8, '\u5728\u5efa'), (9, '\u7ae3\u5de5\u5ba1\u6838'), (10, '\u5b8c\u7ed3')], default=0, verbose_name='\u5f53\u524d\u6d41\u7a0b'),
        ),
    ]
