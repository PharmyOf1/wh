# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-05 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0009_auto_20160529_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blackouts',
            name='apr_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='apr_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='aug_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='aug_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='dec_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='dec_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='feb_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='feb_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='ibl',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jan_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jan_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jul_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jul_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jun_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='jun_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='line_number',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='mar_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='mar_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='may_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='may_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='nov_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='nov_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='oct_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='oct_straight',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='prod_type',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='sep_ot',
        ),
        migrations.RemoveField(
            model_name='blackouts',
            name='sep_straight',
        ),
        migrations.AddField(
            model_name='blackouts',
            name='label',
            field=models.CharField(blank=True, db_column='LABEL', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='blackouts',
            name='shifts',
            field=models.CharField(blank=True, db_column='SHIFTS', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='blackouts',
            name='week_date',
            field=models.CharField(blank=True, db_column='WEEK_DATE', max_length=40, null=True),
        ),
    ]