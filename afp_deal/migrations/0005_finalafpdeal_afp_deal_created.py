# Generated by Django 3.2 on 2022-03-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0004_afpdeal_afp_deal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalafpdeal',
            name='afp_deal_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]