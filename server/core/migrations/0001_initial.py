# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 11:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('measure_unit', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Public_key',
            fields=[
                ('key_hash', models.CharField(blank=True, max_length=64, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('public_key', models.TextField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='T_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_index', models.IntegerField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('input_index', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('t_hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('server_timestamp', models.DateTimeField(auto_now=True)),
                ('client_timestamp', models.DateTimeField()),
                ('batch_id', models.CharField(max_length=64, null=True)),
                ('origin', models.CharField(max_length=64, null=True)),
                ('destination', models.CharField(max_length=64, null=True)),
                ('operator', models.CharField(max_length=64, null=True)),
                ('sign', models.CharField(max_length=256)),
                ('data_string', models.CharField(max_length=1000)),
                ('transmitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Public_key')),
            ],
        ),
        migrations.AddField(
            model_name='t_item',
            name='input_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input', to='core.Transaction'),
        ),
        migrations.AddField(
            model_name='t_item',
            name='output_transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='core.Transaction'),
        ),
        migrations.AddField(
            model_name='t_item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product'),
        ),
        migrations.AddField(
            model_name='t_item',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Public_key'),
        ),
        migrations.AlterUniqueTogether(
            name='t_item',
            unique_together=set([('output_transaction', 'output_index')]),
        ),
    ]
