# Generated by Django 4.1.1 on 2024-03-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_trn_entry_sch_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='unsd_entry',
            name='mode_trn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='sop_ver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trn_attend_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trn_edit_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trn_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trn_start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trnr_dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trnr_desn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='trnr_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='type_trn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='vanue',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='viva_voice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='written_test',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
