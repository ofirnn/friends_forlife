# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='type',
        ),
        migrations.AddField(
            model_name='dog',
            name='is_children_friendly',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='is_hypoallergenic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dog',
            name='type_name',
            field=models.CharField(help_text=b'The name of the Dog-type', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='DogType',
        ),
    ]
