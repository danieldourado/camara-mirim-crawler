# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-06 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0006_auto_20180306_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='texto2',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
