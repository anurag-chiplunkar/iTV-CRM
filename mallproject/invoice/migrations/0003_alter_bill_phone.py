# Generated by Django 4.0.1 on 2022-01-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_bill_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='phone',
            field=models.IntegerField(max_length=2000),
        ),
    ]
