# Generated by Django 3.1.14 on 2022-01-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_dataset_glosslanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gloss',
            name='alternating_movement',
            field=models.BooleanField(default=False, null=True, verbose_name='Alternating Movement'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='repeated_movement',
            field=models.BooleanField(default=False, null=True, verbose_name='Repeated Movement'),
        ),
    ]
