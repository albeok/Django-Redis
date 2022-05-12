# Generated by Django 4.0.4 on 2022-05-11 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_delete_lot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_code', models.CharField(max_length=20)),
                ('tracking_code', models.CharField(max_length=10)),
                ('product', models.CharField(max_length=30)),
                ('production_quantity', models.CharField(max_length=10)),
                ('date_time_arrival', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_time_production', models.DateTimeField(default=django.utils.timezone.now)),
                ('manufacturing_plant', models.CharField(max_length=30)),
                ('recipient', models.CharField(max_length=20)),
                ('tx_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lot',
                'verbose_name_plural': 'Lot',
            },
        ),
    ]
