# Generated by Django 5.1.3 on 2024-12-23 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_alter_tbl_supervisor_supervisor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_stafftype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stafftype_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_contact', models.CharField(max_length=30)),
                ('staff_email', models.CharField(max_length=30)),
                ('staff_password', models.CharField(max_length=30)),
                ('staff_status', models.CharField(max_length=30)),
                ('staff_photo', models.FileField(upload_to='Assets/Files/User')),
                ('stype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_stafftype')),
            ],
        ),
    ]
