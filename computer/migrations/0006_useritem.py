# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0005_auto_20170803_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(default='', max_length=50)),
                ('iid', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
