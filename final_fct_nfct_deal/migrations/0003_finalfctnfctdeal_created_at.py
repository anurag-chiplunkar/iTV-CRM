# Generated by Django 3.2.11 on 2022-03-03 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('final_fct_nfct_deal', '0002_auto_20220303_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalfctnfctdeal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
