# Generated by Django 3.2.11 on 2022-01-20 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_auto_20220121_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencycontact',
            name='agency_details',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='agency.agencydetail'),
        ),
    ]