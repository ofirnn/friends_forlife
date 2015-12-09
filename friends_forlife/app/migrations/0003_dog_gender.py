# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151126_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
