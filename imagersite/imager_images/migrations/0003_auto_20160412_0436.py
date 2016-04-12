# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20160412_0347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='imager_profile.User_Profile'),
        ),
    ]
