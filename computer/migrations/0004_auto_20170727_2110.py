# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0003_auto_20170727_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]
