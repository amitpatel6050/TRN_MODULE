# Generated by Django 4.1.1 on 2024-03-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0068_unsd_entry_unsd_exit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='emp_name_assign',
            field=models.CharField(max_length=100, null=True),
        ),
    ]