# Generated by Django 3.2 on 2022-02-24 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency_client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalFctNfctDeal',
            fields=[
                ('deal_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('fct_total', models.IntegerField(blank=True, null=True)),
                ('nfct_total', models.IntegerField(blank=True, null=True)),
                ('grandtotal', models.IntegerField(blank=True, null=True)),
                ('agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencycontact')),
                ('agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
                ('brand_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='agency_client.customername')),
                ('client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customercontact')),
                ('client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='client', to='agency_client.customername')),
            ],
        ),
    ]
