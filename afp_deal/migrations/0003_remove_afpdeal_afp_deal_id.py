# Generated by Django 3.2 on 2022-03-03 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0002_auto_20220303_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afpdeal',
            name='afp_deal_id',
        ),
    ]