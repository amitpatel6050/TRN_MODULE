# Generated by Django 4.1.1 on 2024-03-27 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0070_unsd_entry_emp_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trn_entry',
            name='type_trn',
        ),
    ]