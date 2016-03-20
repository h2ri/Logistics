# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('addressLogitude', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectorPinCodeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collectors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('addressLatitude', models.FloatField(null=True, blank=True)),
                ('addressLogitude', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('postalCode', models.IntegerField(serialize=False, primary_key=True)),
                ('Locality', models.CharField(max_length=255, null=True, blank=True)),
                ('Active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='collectorpincoderelation',
            name='collector',
            field=models.ForeignKey(related_name='acollectors', to='Collectors.Collectors'),
        ),
        migrations.AddField(
            model_name='collectorpincoderelation',
            name='postalCode',
            field=models.ForeignKey(related_name='Collection_postal_Code', to='Collectors.PostalCode'),
        ),
        migrations.AddField(
            model_name='clients',
            name='postalCode',
            field=models.ForeignKey(related_name='postal_Code', to='Collectors.PostalCode'),
        ),
    ]
