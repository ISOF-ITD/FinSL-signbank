# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20170511_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glossvideo',
            options={'ordering': ['version'], 'verbose_name': 'Gloss video', 'verbose_name_plural': 'Gloss videos'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]
