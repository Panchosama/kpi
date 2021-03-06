# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-26 16:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180926_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='departamento',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='area', chained_model_field='area', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Departamento'),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='responsable',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='departamento', chained_model_field='departamento', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cargo'),
        ),
    ]
