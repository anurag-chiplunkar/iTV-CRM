# Generated by Django 3.2.6 on 2022-03-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_fct_nonfct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fct_deal',
            name='fct1',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='fct_deal',
            name='fct2',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='fct_deal',
            name='fct3',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
