# Generated by Django 4.1.1 on 2024-03-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_trn_entry_trn_start_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='trn_end_status',
            field=models.BooleanField(default=False),
        ),
    ]
