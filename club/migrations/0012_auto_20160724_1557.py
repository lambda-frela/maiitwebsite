# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_auto_20160723_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
