# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 19:03
from __future__ import unicode_literals

# These migrations should only be run during tests and not in your installed app.
try:
    raise ImportError()
    import django.contrib.postgres.fields.jsonb
    json_field = django.contrib.postgres.fields.jsonb.JSONField()
except ImportError:
    import jsonfield.fields
    json_field = jsonfield.fields.JSONField()
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MetricRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_value', models.FloatField(default=0)),
                ('data', json_field),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue', models.FloatField(null=True)),
                ('margin', models.FloatField()),
                ('margin_percent', models.FloatField()),
                ('time', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Uniques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=16, unique=True)),
                ('field2', models.CharField(max_length=16, unique=True)),
                ('field3', models.CharField(max_length=16)),
                ('field4', models.CharField(default=b'default_value', max_length=16)),
                ('field5', models.CharField(default=None, max_length=16, null=True)),
                ('field6', models.CharField(max_length=16)),
                ('field7', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='uniques',
            unique_together=set([('field6', 'field7')]),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tests.User'),
        ),
    ]
