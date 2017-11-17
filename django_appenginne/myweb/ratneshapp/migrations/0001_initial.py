# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-07 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'online',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='pictures')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='RatneshPy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('online', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratneshapp.Online')),
            ],
            options={
                'db_table': 'ratneshpy',
            },
        ),
    ]