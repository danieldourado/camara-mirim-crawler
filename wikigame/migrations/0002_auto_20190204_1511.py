# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-04 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikigame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikigame',
            name='texto',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='wikitermos',
            name='alias_in_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]
