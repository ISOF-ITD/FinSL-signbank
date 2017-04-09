# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import signbank.video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20161201_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossvideo',
            name='dataset',
            field=models.ForeignKey(help_text='Dataset of a GlossVideo, derived from gloss (if any) or chosen when video was uploaded.', null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.Dataset', verbose_name='Glossvideo dataset'),
        ),
        migrations.AlterField(
            model_name='glossvideo',
            name='gloss',
            field=models.ForeignKey(help_text='The gloss this GlossVideo is related to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.Gloss', verbose_name='Gloss'),
        ),
        migrations.AlterField(
            model_name='glossvideo',
            name='posterfile',
            field=models.FileField(help_text='Still image representation of the video.', null=True, storage=signbank.video.models.GlossVideoStorage(), upload_to=b'glossvideo/posters', verbose_name='Poster file'),
        ),
        migrations.AlterField(
            model_name='glossvideo',
            name='title',
            field=models.CharField(blank=True, help_text='Descriptive name of the video.', max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='glossvideo',
            name='version',
            field=models.IntegerField(default=0, help_text="A number that represents the order of the Glossvideo's in a gloss page. Smaller number means higher priority.", verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='glossvideo',
            name='videofile',
            field=models.FileField(help_text='Video file.', storage=signbank.video.models.GlossVideoStorage(), upload_to=b'glossvideo', verbose_name='Video file'),
        ),
    ]