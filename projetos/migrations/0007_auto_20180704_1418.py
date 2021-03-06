# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-04 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0006_projeto_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='ano',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='cep',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='cidade',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='dataDeNascimento',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='endereco',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='escola',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nomeDaCrianca',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nomeDoProjetoDeLei',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nomeDosPais',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='serie',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='sexo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='telefone',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tema',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='uf',
            field=models.TextField(),
        ),
    ]
