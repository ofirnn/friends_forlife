# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151211_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='dog',
            name='age',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
