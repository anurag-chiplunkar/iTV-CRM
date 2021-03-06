# Generated by Django 3.2.11 on 2022-02-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AFP_Base_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afp_unique_key', models.CharField(blank=True, max_length=100, null=True)),
                ('baserate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AFP_Channels',
            fields=[
                ('channels', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AFP_ProgramName',
            fields=[
                ('program_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('b_list', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='base_rate_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(blank=True, default='default', max_length=100, null=True)),
                ('br', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChannelNFCT',
            fields=[
                ('channel', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disper',
            fields=[
                ('dis_list', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Events_Category',
            fields=[
                ('category_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='fct_deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chan', models.CharField(blank=True, max_length=255, null=True)),
                ('dis', models.CharField(blank=True, max_length=255, null=True)),
                ('band1', models.CharField(blank=True, max_length=255, null=True)),
                ('band2', models.CharField(blank=True, max_length=255, null=True)),
                ('band3', models.CharField(blank=True, max_length=255, null=True)),
                ('fct1', models.IntegerField(blank=True, null=True)),
                ('fct2', models.IntegerField(blank=True, null=True)),
                ('fct3', models.IntegerField(blank=True, null=True)),
                ('eff_rate1', models.IntegerField(blank=True, null=True)),
                ('eff_rate2', models.IntegerField(blank=True, null=True)),
                ('eff_rate3', models.IntegerField(blank=True, null=True)),
                ('rev1', models.IntegerField(blank=True, null=True)),
                ('rev2', models.IntegerField(blank=True, null=True)),
                ('rev3', models.IntegerField(blank=True, null=True)),
                ('total_rev', models.IntegerField()),
                ('prev_yr_fct', models.IntegerField(blank=True, null=True)),
                ('curr_fct', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events_Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('merit_money', models.CharField(max_length=200)),
                ('ref_category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_afp.events_category')),
                ('ref_channels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_afp.afp_channels')),
            ],
        ),
        migrations.CreateModel(
            name='AFP_Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promos', models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30')], max_length=20, null=True)),
                ('slot', models.CharField(blank=True, choices=[('10', '10'), ('22', '22')], max_length=20, null=True)),
                ('eff_rate', models.CharField(max_length=200)),
                ('ref_channels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_afp.afp_channels')),
                ('ref_program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_afp.afp_programname')),
            ],
        ),
    ]
