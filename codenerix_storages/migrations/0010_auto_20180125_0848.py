# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-25 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_storages', '0009_auto_20180119_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryline',
            name='caducity',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Caducity'),
        ),
        migrations.AddField(
            model_name='inventoryline',
            name='product_unique_value',
            field=models.CharField(blank=True, default=None, editable=False, max_length=80, null=True, verbose_name='Product Unique Value'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ends'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Starts'),
        ),
        migrations.AlterField(
            model_name='inventoryline',
            name='product_unique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='storage_inventorylines', to='codenerix_products.ProductUnique', verbose_name='Product Unique'),
        ),
    ]
