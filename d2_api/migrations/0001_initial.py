# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=16)),
                ('user_id', models.CharField(max_length=20)),
            ],
        ),
    ]
