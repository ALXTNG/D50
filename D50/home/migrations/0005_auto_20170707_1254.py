# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170706_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('can_drive', 'Can drive'), ('can_vote', 'Can vote in elections'), ('can_drink', 'Can drink alcohol'))},
        ),
    ]
