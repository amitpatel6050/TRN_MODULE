# Generated by Django 4.1.1 on 2023-11-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_alter_user_trn_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_trn',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
