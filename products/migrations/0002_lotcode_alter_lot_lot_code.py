# Generated by Django 4.0.4 on 2022-05-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='lot_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.lotcode'),
        ),
    ]