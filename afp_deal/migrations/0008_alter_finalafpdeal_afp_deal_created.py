# Generated by Django 3.2 on 2022-03-03 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0007_alter_finalafpdeal_afp_deal_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalafpdeal',
            name='afp_deal_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 13, 57, 15, 456690)),
        ),
    ]
