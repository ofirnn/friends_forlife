# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(help_text=b'The name of the Dog', max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=100, null=True)),
                ('is_adopted', models.BooleanField(default=False)),
                ('is_castrated', models.BooleanField(default=False)),
                ('is_educated', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(help_text=b'State Name - In-Adoption / In-House / Treatment ', max_length=50)),
                ('picture', models.ImageField(default=b'media/dog_pictures/no-img.jpg', upload_to=b'dog_pictures')),
                ('chip_id', models.CharField(help_text=b'IL chip-id', max_length=200)),
                ('size', models.CharField(max_length=200, null=True)),
                ('type_name', models.CharField(help_text=b'The name of the Dog-type', max_length=200, null=True)),
                ('is_hypoallergenic', models.BooleanField(default=False)),
                ('is_children_friendly', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DogHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(help_text=b'Name of doghouse owner', max_length=200)),
                ('owner_phone', models.CharField(help_text=b'Phone Number of owner', max_length=200)),
                ('owner_email', models.EmailField(help_text=b'Email of doghouse owner', max_length=254)),
                ('owner_city', models.CharField(max_length=50)),
                ('address', models.CharField(help_text=b'Full-Address Of DogHouse', max_length=500)),
                ('capacity', models.IntegerField(help_text=b'Maximum dogs capacity')),
            ],
        ),
        migrations.CreateModel(
            name='DogStaying',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(null=True)),
                ('dog', models.ForeignKey(to='app.Dog')),
                ('house', models.ForeignKey(to='app.DogHouse')),
            ],
        ),
        migrations.CreateModel(
            name='DonationBasket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='app.BasketItem')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('ils_value', models.FloatField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='stayings',
            field=models.ManyToManyField(to='app.DogHouse', null=True, through='app.DogStaying'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='item',
            field=models.ForeignKey(to='app.Item'),
        ),
    ]
