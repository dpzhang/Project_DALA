# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170309_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testchoice',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
