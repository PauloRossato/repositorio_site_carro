# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='valor',
            field=models.FloatField(default=0, verbose_name=10000),
            preserve_default=False,
        ),
    ]
