# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151209_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.ImageField(default=b'media/dog_pictures/no-img.jpg', upload_to=b'media/dog_pictures/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='stayings',
            field=models.ManyToManyField(to='app.DogStaying', null=True),
        ),
    ]
