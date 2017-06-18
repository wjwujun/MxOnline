# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170611_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default=1, upload_to='banner/%Y/%m', verbose_name='轮播图'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '忘记密码')], max_length=50),
        ),
    ]
