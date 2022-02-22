# Generated by Django 3.2 on 2022-02-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('agency', '0002_alter_agencydetail_agency_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalFctNfctDeal',
            fields=[
                ('deal_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fct_total', models.IntegerField()),
                ('nfct_total', models.IntegerField()),
                ('grandtotal', models.IntegerField()),
                ('agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency.agencycontact')),
                ('agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency.agencydetail')),
                ('client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='customer.customercontact')),
                ('client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='customer.customername')),
            ],
        ),
    ]
