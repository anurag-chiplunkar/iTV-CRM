# Generated by Django 3.2 on 2022-02-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_fct_nonfct', '0004_auto_20220205_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='fct_deal',
            name='chan',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]