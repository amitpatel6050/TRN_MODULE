# Generated by Django 4.1.1 on 2024-03-22 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_rename_sop_no_unsd_entry_sop_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unsd_entry',
            name='sop_name',
        ),
        migrations.RemoveField(
            model_name='unsd_entry',
            name='sop_num',
        ),
    ]
