# Generated by Django 4.1.1 on 2023-05-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_user_rgp_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='nrgp_entry',
            name='nrgp_main_serial',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
    ]
