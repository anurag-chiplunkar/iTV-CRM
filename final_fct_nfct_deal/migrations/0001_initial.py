# Generated by Django 3.2.6 on 2022-03-04 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency_client', '0002_alter_agencydetail_agency_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalFctNfctDeal',
            fields=[
                ('deal_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('executive', models.CharField(max_length=255)),
                ('reporting_manager', models.CharField(max_length=255)),
                ('RO_number', models.CharField(max_length=255)),
                ('RO_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('fct_total', models.IntegerField(blank=True, default='0', null=True)),
                ('nfct_total', models.IntegerField(blank=True, default='0', null=True)),
                ('grandtotal', models.IntegerField(blank=True, null=True)),
                ('agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencycontact')),
                ('agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
                ('brand_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='agency_client.customername')),
                ('client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customercontact')),
                ('client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='client', to='agency_client.customername')),
            ],
        ),
    ]
