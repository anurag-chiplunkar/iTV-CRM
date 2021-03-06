# Generated by Django 3.2 on 2022-02-06 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('customer_type', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerName',
            fields=[
                ('cname', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ref_customertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customertype')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('pri_fname', models.CharField(max_length=50)),
                ('pri_lname', models.CharField(max_length=50)),
                ('pri_desg', models.CharField(max_length=50)),
                ('pri_email', models.EmailField(max_length=254)),
                ('pri_phone', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('pri_landline', models.CharField(max_length=15)),
                ('pri_flatno', models.CharField(max_length=10)),
                ('pri_streetname', models.CharField(max_length=100)),
                ('pri_landmark', models.CharField(max_length=100)),
                ('pri_city', models.CharField(max_length=50)),
                ('pri_pincode', models.CharField(max_length=10)),
                ('sec_fname', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_lname', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_desg', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sec_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('sec_landline', models.CharField(blank=True, max_length=15, null=True)),
                ('sec_flatno', models.CharField(blank=True, max_length=10, null=True)),
                ('sec_streetname', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_city', models.CharField(blank=True, max_length=50, null=True)),
                ('sec_pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('ref_cname', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='customer.customername')),
            ],
        ),
    ]
