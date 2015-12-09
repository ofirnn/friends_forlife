# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_dog_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.ImageField(default=b'dogs_pictures/no-img.jpg', upload_to=b'dog_pictures/'),
        ),
    ]
