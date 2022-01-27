# Generated by Django 3.2.11 on 2022-01-20 15:10

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
                ('a_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('agency_name', models.CharField(max_length=200)),
                ('agency_state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AgencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('agency_details', models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='agency.agencydetail')),
            ],
        ),
    ]
