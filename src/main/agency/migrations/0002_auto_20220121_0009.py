# Generated by Django 3.2.11 on 2022-01-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agencycontact',
            name='id',
        ),
        migrations.AddField(
            model_name='agencycontact',
            name='ac_id',
            field=models.CharField(default='default', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='agencydetail',
            name='a_id',
            field=models.CharField(default='default', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
