# Generated by Django 3.2.11 on 2022-02-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deal_nfct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_id', models.CharField(default=None, max_length=500)),
                ('channel', models.CharField(choices=[('INN', 'INN'), ('NX', 'NX'), ('GUJ', 'GUJ'), ('PUN', 'PUN')], max_length=255)),
                ('element', models.CharField(choices=[('Aston', 'Aston'), ('L Band', 'L Band'), ('Logo Bug', 'Logo Bug')], max_length=255)),
                ('durations', models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months')], max_length=6, null=True)),
                ('duration_in', models.IntegerField(blank=True, null=True)),
                ('er', models.IntegerField(blank=True, null=True)),
                ('freq', models.IntegerField(blank=True, null=True)),
                ('total_seconds', models.IntegerField(blank=True, null=True)),
                ('base_rate', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NFCT_Base_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfct_unique_key', models.CharField(blank=True, max_length=100, null=True)),
                ('channel', models.CharField(choices=[('INN', 'INN'), ('NX', 'NX'), ('GUJ', 'GUJ'), ('PUN', 'PUN')], max_length=255)),
                ('element', models.CharField(choices=[('Aston', 'Aston'), ('L Band', 'L Band'), ('Logo Bug', 'Logo Bug')], max_length=255)),
                ('nfct_baserate', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
