# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courses_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='http://baidu.com', max_length=200, verbose_name='访问地址'),
        ),
    ]
