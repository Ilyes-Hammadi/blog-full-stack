# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles/'),
        ),
    ]
