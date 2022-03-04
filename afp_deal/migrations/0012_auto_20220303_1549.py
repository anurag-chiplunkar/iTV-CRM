# Generated by Django 3.2 on 2022-03-03 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afp_deal', '0011_alter_afpdeal_ref_program_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afpdeal',
            name='afp_base_rate',
            field=models.IntegerField(verbose_name='base Rate'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='afp_eff_rate',
            field=models.CharField(max_length=200, verbose_name='effective Rate'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_channels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp_deal.afpchannels', verbose_name='channel'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_program_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp_deal.afpprogramname', verbose_name='program Name'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_promos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp_deal.afppromos', verbose_name='promo'),
        ),
        migrations.AlterField(
            model_name='afpdeal',
            name='ref_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afp_deal.afpslots', verbose_name='slot'),
        ),
    ]
