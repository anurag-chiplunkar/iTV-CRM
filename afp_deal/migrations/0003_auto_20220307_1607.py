# Generated by Django 3.2 on 2022-03-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0002_afpdeal_afp_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_program_name',
            field=models.CharField(max_length=200, verbose_name='program Name'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_promos',
            field=models.CharField(max_length=200, verbose_name='promos'),
        ),
    ]
