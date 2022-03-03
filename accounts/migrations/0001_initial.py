# Generated by Django 3.2 on 2022-02-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_fname', models.CharField(max_length=50)),
                ('emp_lname', models.CharField(max_length=50)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_phone', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('emp_desgn', models.CharField(max_length=100)),
                ('emp_reporting_mgr', models.CharField(max_length=100)),
                ('emp_pass1', models.CharField(max_length=100)),
                ('emp_pass2', models.CharField(max_length=100)),
            ],
        ),
    ]
