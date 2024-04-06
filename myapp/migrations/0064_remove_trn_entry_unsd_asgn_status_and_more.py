# Generated by Django 4.1.1 on 2024-03-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0063_trn_entry_unsd_asgn_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_asgn_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_assign_time',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_attend_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_attend_time',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_edit_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_edit_time',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_end_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_end_time',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_evalu_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_start_status',
        ),
        migrations.RemoveField(
            model_name='trn_entry',
            name='unsd_start_time',
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_asgn_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_assign_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_attend_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_attend_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_edit_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_edit_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_end_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_evalu_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_start_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unsd_entry',
            name='unsd_start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
