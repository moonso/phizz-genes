# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genes', '0003_auto_20160929_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='entrez_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='hgnc_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ucsc_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='vega_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transcript',
            name='refseq_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
