# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20170620_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='portfolio',
            new_name='website',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='user_img'),
        ),
    ]
