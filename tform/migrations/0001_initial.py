# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DataUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_description', models.CharField(blank=True, max_length=100, null=True)),
                ('file_upload', models.FileField(null=True, upload_to='doc')),
                ('file_time_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.IntegerField()),
                ('q_item', models.CharField(max_length=50)),
                ('q_index', models.CharField(max_length=200)),
                ('q_explanation', models.CharField(max_length=200)),
                ('q_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='tform.Category')),
                ('q_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method', to='tform.Method')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField(default=1)),
                ('evidence', models.CharField(blank=True, max_length=200)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='tform.Project')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_items', to='tform.Question')),
                ('result_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dataupload', to='tform.DataUpload')),
            ],
        ),
        migrations.CreateModel(
            name='StarLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_name', models.CharField(default='3', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(default='pending', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='tform.Status'),
        ),
        migrations.AddField(
            model_name='question',
            name='q_star',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='star_level', to='tform.StarLevel'),
        ),
    ]
