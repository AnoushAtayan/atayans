# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_store_store_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterField(
            model_name='store',
            name='store_link',
            field=models.CharField(max_length=120),
        ),
        migrations.AddField(
            model_name='comment',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Store'),
        ),
    ]
