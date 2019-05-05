# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-26 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190426_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='名称'),
        ),
    ]