# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-26 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180926_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
