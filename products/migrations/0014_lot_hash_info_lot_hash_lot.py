# Generated by Django 4.0.4 on 2022-05-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_lot_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='hash_info',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='lot',
            name='hash_lot',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
