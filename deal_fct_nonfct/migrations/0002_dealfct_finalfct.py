# Generated by Django 3.2.11 on 2022-03-03 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency_client', '0002_alter_agencydetail_agency_pin'),
        ('deal_fct_nonfct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealFct',
            fields=[
                ('dealid_fct', models.CharField(default='default', max_length=100, primary_key=True, serialize=False)),
                ('chan', models.CharField(blank=True, max_length=1000, null=True)),
                ('dis', models.CharField(blank=True, max_length=1000, null=True)),
                ('band1', models.CharField(blank=True, max_length=1000, null=True)),
                ('band2', models.CharField(blank=True, max_length=1000, null=True)),
                ('band3', models.CharField(blank=True, max_length=1000, null=True)),
                ('fct1', models.IntegerField(blank=True, null=True)),
                ('fct2', models.IntegerField(blank=True, null=True)),
                ('fct3', models.IntegerField(blank=True, null=True)),
                ('eff_rate1', models.IntegerField(blank=True, null=True)),
                ('eff_rate2', models.IntegerField(blank=True, null=True)),
                ('eff_rate3', models.IntegerField(blank=True, null=True)),
                ('rev1', models.IntegerField(blank=True, null=True)),
                ('rev2', models.IntegerField(blank=True, null=True)),
                ('rev3', models.IntegerField(blank=True, null=True)),
                ('total_rev', models.IntegerField(blank=True, null=True)),
                ('base_rate1', models.IntegerField(blank=True, null=True)),
                ('base_rate2', models.IntegerField(blank=True, null=True)),
                ('base_rate3', models.IntegerField(blank=True, null=True)),
                ('prev_yr_fct', models.IntegerField(blank=True, null=True)),
                ('curr_fct', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinalFCT',
            fields=[
                ('deal_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('executive', models.CharField(max_length=255)),
                ('reporting_manager', models.CharField(max_length=255)),
                ('RO_number', models.CharField(max_length=255)),
                ('RO_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencycontact')),
                ('agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
                ('brand_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='brandfct', to='agency_client.customername')),
                ('client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customercontact')),
                ('client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='clientfct', to='agency_client.customername')),
            ],
        ),
    ]
