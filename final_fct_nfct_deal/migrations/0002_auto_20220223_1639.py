# Generated by Django 3.2.6 on 2022-02-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_fct_nfct_deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalfctnfctdeal',
            name='deal_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='finalfctnfctdeal',
            name='grandtotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
