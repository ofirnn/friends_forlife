# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151211_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='stayings',
            field=models.ManyToManyField(to='app.DogStaying', blank=True),
        ),
    ]
