# Generated by Django 4.1.1 on 2024-04-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0078_alter_user_trn_department_alter_user_trn_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sop_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sop_name', models.CharField(max_length=100)),
                ('sop_no', models.CharField(max_length=100)),
            ],
        ),
    ]