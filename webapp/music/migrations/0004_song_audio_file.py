# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20171227_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=b''),
        ),
    ]
