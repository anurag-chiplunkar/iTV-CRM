# Generated by Django 3.2 on 2022-03-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0008_alter_finalafpdeal_afp_deal_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalafpdeal',
            name='afp_deal_created',
            field=models.DateTimeField(),
        ),
    ]
