# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-05 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0012_auto_20160605_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackouts',
            name='file_name',
            field=models.CharField(blank=True, db_column='FILE_NAME', max_length=40, null=True),
        ),
    ]
