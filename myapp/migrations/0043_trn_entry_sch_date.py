# Generated by Django 4.1.1 on 2024-03-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_trn_entry_sop_assign_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='sch_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]