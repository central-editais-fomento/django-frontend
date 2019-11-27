# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-11-01 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumo', models.CharField(max_length=1000)),
                ('texto', models.TextField()),
                ('data_limite', models.DateField()),
                ('areas', models.CharField(max_length=1000)),
                ('tipos', models.CharField(max_length=1000)),
            ],
        ),
    ]