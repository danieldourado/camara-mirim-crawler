# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-06 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0010_auto_20180306_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='texto',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='texto2',
            field=models.TextField(default=''),
        ),
    ]
