# Generated by Django 4.1.1 on 2024-03-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_rename_rgp_entry_trn_entry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='sop_ver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trn_entry',
            name='trnr_dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trn_entry',
            name='trnr_desn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trn_entry',
            name='trnr_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trn_entry',
            name='vanue',
            field=models.CharField(max_length=100, null=True),
        ),
    ]