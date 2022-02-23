# Generated by Django 3.2.11 on 2022-02-23 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercontact',
            name='ref_cname',
            field=models.ForeignKey(default='default', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cust_name', to='agency_client.customername'),
        ),
    ]
