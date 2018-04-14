# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-14 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0017_cashdiary_cashmovement'),
        ('codenerix_storages', '0022_auto_20180414_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryinline',
            name='purchaseslinealbaran',
        ),
        migrations.AddField(
            model_name='inventoryinline',
            name='purchaseslinealbaran',
            field=models.ManyToManyField(related_name='inventory_lines', to='codenerix_invoicing.PurchasesLineAlbaran', verbose_name='Line Albaran'),
        ),
    ]
