# Generated by Django 3.2.11 on 2022-03-03 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfct', '0004_auto_20220303_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealnfctgrandtotal',
            old_name='nfct_grandtotal',
            new_name='nfct_grand_total',
        ),
        migrations.RemoveField(
            model_name='finalnfct',
            name='nfct_total',
        ),
    ]
