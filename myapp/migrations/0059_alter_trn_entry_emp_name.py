# Generated by Django 4.1.1 on 2024-03-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0058_alter_trn_entry_emp_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trn_entry',
            name='emp_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]