# Generated by Django 4.1.1 on 2024-03-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_trn_entry_sop_ver_trn_entry_trnr_dept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='trn_update_time',
            field=models.DateTimeField(null=True),
        ),
    ]
