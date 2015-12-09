# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151209_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.ImageField(default=b'media/dogs_pictures/no-img.jpg', upload_to=b'media/dog_pictures/'),
        ),
    ]
