# Generated by Django 4.1.1 on 2024-03-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0064_remove_trn_entry_unsd_asgn_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unsd_entry',
            name='unsd_attend_time',
        ),
        migrations.RemoveField(
            model_name='unsd_entry',
            name='unsd_edit_time',
        ),
    ]