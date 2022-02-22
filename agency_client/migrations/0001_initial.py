# Generated by Django 3.2.11 on 2022-02-22 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyDetail',
            fields=[
                ('a_id', models.CharField(default='default', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('agency_name', models.CharField(max_length=200)),
                ('agency_officeno', models.CharField(max_length=10)),
                ('agency_street', models.CharField(max_length=100)),
                ('agency_state', models.CharField(max_length=50)),
                ('agency_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('agency_city', models.CharField(max_length=100)),
                ('agency_pin', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('customer_type', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerName',
            fields=[
                ('creg_no', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('cname', models.CharField(max_length=200)),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ref_customertype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agency_client.customertype')),
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
                ('ref_creg_no', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customername')),
            ],
        ),
        migrations.CreateModel(
            name='AgencyContact',
            fields=[
                ('pri_firstName', models.CharField(max_length=20)),
                ('pri_lastName', models.CharField(max_length=20)),
                ('pri_designation', models.CharField(max_length=100)),
                ('pri_email', models.EmailField(max_length=254)),
                ('pri_phone', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('pri_landline', models.CharField(max_length=20)),
                ('pri_flatno', models.CharField(max_length=10)),
                ('pri_street', models.CharField(max_length=100)),
                ('pri_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('pri_city', models.CharField(max_length=100)),
                ('pri_pin', models.CharField(max_length=10)),
                ('sec_firstName', models.CharField(blank=True, max_length=20, null=True)),
                ('sec_lastName', models.CharField(blank=True, max_length=20, null=True)),
                ('sec_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sec_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('sec_landline', models.CharField(blank=True, max_length=20, null=True)),
                ('sec_flatno', models.CharField(blank=True, max_length=10, null=True)),
                ('sec_street', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_city', models.CharField(blank=True, max_length=100, null=True)),
                ('sec_pin', models.CharField(blank=True, max_length=10, null=True)),
                ('agency_details', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
            ],
        ),
    ]
