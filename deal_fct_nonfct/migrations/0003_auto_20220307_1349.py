# Generated by Django 3.2.9 on 2022-03-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_fct_nonfct', '0002_auto_20220304_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealfct',
            name='eff_rate1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='eff_rate2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='eff_rate3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='rev1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='rev2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='rev3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dealfct',
            name='total_rev',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finalfct',
            name='fct_total_rev',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]