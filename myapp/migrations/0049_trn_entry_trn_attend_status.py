# Generated by Django 4.1.1 on 2024-03-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_trn_entry_trn_asgn_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trn_entry',
            name='trn_attend_status',
            field=models.BooleanField(default=False),
        ),
    ]