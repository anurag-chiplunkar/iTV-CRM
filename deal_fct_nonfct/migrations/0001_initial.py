# Generated by Django 3.2.11 on 2022-03-07 20:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency_client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('b_list', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.CharField(blank=True, choices=[('INN', 'INN'), ('NX', 'NX'), ('IN UP', 'IN UP'), ('MP', 'MP'), ('RAJ', 'RAJ'), ('PUN', 'PUN'), ('HAR', 'HAR'), ('GUJ', 'GUJ'), ('NE NEWS', 'NE NEWS')], max_length=1000, null=True)),
                ('dispersion', models.CharField(blank=True, max_length=1000, null=True)),
                ('bands', models.CharField(blank=True, max_length=1000, null=True)),
                ('br', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Base_rate_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(blank=True, default='default', max_length=255, null=True)),
                ('br', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('c_list', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
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
                ('eff_rate1', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('eff_rate2', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('eff_rate3', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev1', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev2', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev3', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_rev', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('base_rate1', models.IntegerField(blank=True, default='0', null=True)),
                ('base_rate2', models.IntegerField(blank=True, default='0', null=True)),
                ('base_rate3', models.IntegerField(blank=True, default='0', null=True)),
                ('prev_yr_fct', models.IntegerField(blank=True, null=True)),
                ('curr_fct', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disper',
            fields=[
                ('dis_list', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fct_deal',
            fields=[
                ('dealid_fct_ref', models.CharField(default='default', max_length=100, primary_key=True, serialize=False)),
                ('chan', models.CharField(blank=True, max_length=1000, null=True)),
                ('dis', models.CharField(blank=True, max_length=1000, null=True)),
                ('band1', models.CharField(blank=True, max_length=1000, null=True)),
                ('band2', models.CharField(blank=True, max_length=1000, null=True)),
                ('band3', models.CharField(blank=True, max_length=1000, null=True)),
                ('fct1', models.IntegerField(blank=True, default='0', null=True)),
                ('fct2', models.IntegerField(blank=True, default='0', null=True)),
                ('fct3', models.IntegerField(blank=True, default='0', null=True)),
                ('eff_rate1', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('eff_rate2', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('eff_rate3', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev1', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev2', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rev3', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total_rev', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
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
                ('fct_total_rev', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencycontact')),
                ('agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
                ('brand_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='brandfct', to='agency_client.customername')),
                ('client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customercontact')),
                ('client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='clientfct', to='agency_client.customername')),
            ],
        ),
    ]
