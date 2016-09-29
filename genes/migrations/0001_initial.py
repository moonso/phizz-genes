# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgnc_symbol', models.CharField(max_length=20)),
                ('chrom', models.CharField(max_length=30)),
                ('start', models.IntegerField()),
                ('stop', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refseq_name', models.CharField(max_length=30)),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genes.Gene')),
            ],
        ),
    ]
