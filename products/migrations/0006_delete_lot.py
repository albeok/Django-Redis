# Generated by Django 4.0.4 on 2022-05-11 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_lot_generic_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lot',
        ),
    ]
