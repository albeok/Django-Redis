# Generated by Django 4.0.4 on 2022-05-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='hash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
