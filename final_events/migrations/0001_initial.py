# Generated by Django 3.2.11 on 2022-03-07 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency_client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Deal_Nfct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_id_nfct', models.CharField(blank=True, default='default', max_length=255, null=True)),
                ('channel', models.CharField(choices=[('INN', 'INN'), ('NX', 'NX'), ('IN UP', 'IN UP'), ('MP', 'MP'), ('RAJ', 'RAJ'), ('PUN', 'PUN'), ('HAR', 'HAR'), ('GUJ', 'GUJ'), ('NE NEWS', 'NE NEWS')], max_length=255)),
                ('element', models.CharField(choices=[('Aston', 'Aston'), ('L Band', 'L Band'), ('Logo Bug', 'Logo Bug'), ('Headline Sponsership Tag', 'Headline Sponsership Tag'), ('Ticker', 'Ticker'), ('Weather Branding', 'Weather Branding')], max_length=255)),
                ('durations', models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months')], max_length=6, null=True)),
                ('duration_in', models.IntegerField(blank=True, null=True)),
                ('er', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('freq', models.IntegerField(blank=True, null=True)),
                ('total_seconds', models.IntegerField(blank=True, null=True)),
                ('base_rate', models.IntegerField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event_NFCT_Base_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfct_unique_key', models.CharField(blank=True, max_length=100, null=True)),
                ('channel', models.CharField(choices=[('INN', 'INN'), ('NX', 'NX'), ('GUJ', 'GUJ'), ('HAR', 'HAR'), ('MP', 'MP'), ('NE NEWS', 'NE NEWS'), ('PUN', 'PUN'), ('RAJ', 'RAJ'), ('UP', 'UP')], max_length=255)),
                ('element', models.CharField(choices=[('Aston', 'Aston'), ('L Band', 'L Band'), ('Logo Bug', 'Logo Bug'), ('Headline Sponsership Tag', 'Headline Sponsership Tag'), ('Ticker', 'Ticker'), ('Weather Branding', 'Weather Branding')], max_length=255)),
                ('nfct_baserate', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventFCTModel',
            fields=[
                ('deal_id_fct', models.CharField(default='default', max_length=255, primary_key=True, serialize=False)),
                ('chan', models.CharField(blank=True, max_length=1000, null=True)),
                ('dis', models.CharField(blank=True, max_length=1000, null=True)),
                ('band1', models.CharField(blank=True, max_length=1000, null=True)),
                ('band2', models.CharField(blank=True, max_length=1000, null=True)),
                ('band3', models.CharField(blank=True, max_length=1000, null=True)),
                ('fct1', models.IntegerField(blank=True, default=0, null=True)),
                ('fct2', models.IntegerField(blank=True, default=0, null=True)),
                ('fct3', models.IntegerField(blank=True, default=0, null=True)),
                ('eff_rate1', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('eff_rate2', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('eff_rate3', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('rev1', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('rev2', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('rev3', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('total_rev', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=12, null=True)),
                ('base_rate1', models.IntegerField(blank=True, default=0, null=True)),
                ('base_rate2', models.IntegerField(blank=True, default=0, null=True)),
                ('base_rate3', models.IntegerField(blank=True, default=0, null=True)),
                ('prev_yr_fct', models.IntegerField(blank=True, null=True)),
                ('curr_fct', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventNFCTGrandTotal',
            fields=[
                ('dealid_nfct_ref', models.CharField(default='default', max_length=100)),
                ('nfct_grandtotal', models.DecimalField(decimal_places=2, default='0', max_digits=12, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Eventmodel',
            fields=[
                ('deal_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('executive', models.CharField(blank=True, max_length=100, null=True)),
                ('reporting_manager', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(choices=[('Conclave', 'Conclave'), ('Cookery', 'Cookery'), ('Entertainment', 'Entertainment'), ('Fashion', 'Fashion'), ('Health /Life Style', 'Health /Life Style'), ('Infotainment', 'Infotainment'), ('Manch', 'Manch'), ('Politics', 'Politics'), ('Spirituality', 'Spirituality'), ('Sports', 'Sports'), ('Technology', 'Technology'), ('Tourism', 'Tourism')], max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('channel', models.CharField(blank=True, choices=[('INN', 'INN'), ('NX', 'NX'), ('IN UP', 'IN UP'), ('MP', 'MP'), ('RAJ', 'RAJ'), ('PUN', 'PUN'), ('HAR', 'HAR'), ('GUJ', 'GUJ'), ('NE NEWS', 'NE NEWS')], max_length=50, null=True)),
                ('merit_money', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('fct_seconds', models.IntegerField(blank=True, null=True)),
                ('fct_total_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('nfct_total_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('grandtotal_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('ro_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('ro_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_agency_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencycontact')),
                ('event_agency_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.agencydetail')),
                ('event_brand_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='evt_brand', to='agency_client.customername')),
                ('event_client_contact_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency_client.customercontact')),
                ('event_client_name_ref', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='evt_client', to='agency_client.customername')),
            ],
        ),
    ]
