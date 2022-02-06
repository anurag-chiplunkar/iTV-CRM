# Generated by Django 3.2.11 on 2022-02-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20220201_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercontact',
            name='sec_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customercontact',
            name='sec_flatno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customercontact',
            name='sec_landline',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customercontact',
            name='sec_landmark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customercontact',
            name='sec_pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customercontact',
            name='sec_streetname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]