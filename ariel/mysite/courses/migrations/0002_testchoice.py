# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testchoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins1', models.CharField(max_length=30)),
                ('ins2', models.CharField(blank=True, max_length=30)),
                ('ins3', models.CharField(blank=True, max_length=30)),
                ('ins4', models.CharField(blank=True, max_length=30)),
                ('ins5', models.CharField(blank=True, max_length=30)),
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
