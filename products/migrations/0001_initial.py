# Generated by Django 4.0.4 on 2022-05-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('tex_id', models.CharField(max_length=40)),
            ],
        ),
    ]
