# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170722_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal_round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_round', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='proposal',
            new_name='proposals',
        ),
        migrations.RenameField(
            model_name='proposal',
            old_name='respose_scientific_committee',
            new_name='response_scientific_committee',
        ),
        migrations.RenameField(
            model_name='proposal',
            old_name='respose_steering_committee',
            new_name='response_steering_committee',
        ),
        migrations.AddField(
            model_name='proposal',
            name='comments',
            field=models.CharField(blank=True, help_text='add comments, if any', max_length=1000),
        ),
        migrations.AddField(
            model_name='proposal',
            name='proposal_reference_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='proposal_rationale',
            field=models.FileField(blank=True, help_text='this is the rationale of the proposal', upload_to='proposals/'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='proposal_technical_support',
            field=models.FileField(blank=True, help_text='this is the technical addendum of the proposal', upload_to='proposals/'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='proposal_round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Proposal_round'),
        ),
    ]