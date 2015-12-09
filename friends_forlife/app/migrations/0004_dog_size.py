# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_dog_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
