# Generated by Django 5.1.3 on 2024-12-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_tbl_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_supervisor',
            name='supervisor_photo',
            field=models.FileField(upload_to='Assets/Files/User'),
        ),
    ]
