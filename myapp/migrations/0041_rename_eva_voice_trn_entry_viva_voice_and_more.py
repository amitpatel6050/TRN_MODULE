# Generated by Django 4.1.1 on 2024-03-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_trn_entry_eva_voice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trn_entry',
            old_name='eva_voice',
            new_name='viva_voice',
        ),
        migrations.AddField(
            model_name='trn_entry',
            name='written_test',
            field=models.CharField(max_length=100, null=True),
        ),
    ]