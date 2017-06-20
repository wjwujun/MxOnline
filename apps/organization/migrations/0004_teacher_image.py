# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170618_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=1, upload_to='org/teacher/%Y/%m', verbose_name='教师头像'),
            preserve_default=False,
        ),
    ]
