# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170224_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmenttype',
            name='parents',
            field=models.ManyToManyField(related_name='children', to='core.SegmentType', verbose_name='parent type'),
        ),
    ]