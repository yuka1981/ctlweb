# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_dataupload_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_content', models.TextField(blank=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_category', to='report.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='dataupload',
            name='file_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='starlevel',
            name='star_name',
            field=models.CharField(default='3', max_length=20),
        ),
    ]
