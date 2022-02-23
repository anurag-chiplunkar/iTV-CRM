# Generated by Django 3.2 on 2022-02-22 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('final_fct_nfct_deal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalfctnfctdeal',
            name='brand_name_ref',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='customer.customername'),
        ),
        migrations.AlterField(
            model_name='finalfctnfctdeal',
            name='client_name_ref',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='client', to='customer.customername'),
        ),
    ]
