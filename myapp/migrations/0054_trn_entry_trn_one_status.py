# Generated by Django 4.1.1 on 2024-03-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0053_trn_entry_trn_evalu_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='trn_one_status',
            field=models.BooleanField(default=False),
        ),
    ]
