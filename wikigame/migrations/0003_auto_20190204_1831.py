# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-04 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikigame', '0002_auto_20190204_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikigame',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
