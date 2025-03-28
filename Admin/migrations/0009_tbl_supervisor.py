# Generated by Django 5.1.3 on 2024-12-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_name', models.CharField(max_length=30)),
                ('supervisor_contact', models.CharField(max_length=30)),
                ('supervisor_address', models.CharField(max_length=30)),
                ('supervisor_email', models.CharField(max_length=30)),
                ('supervisor_password', models.CharField(max_length=30)),
                ('supervisor_status', models.CharField(max_length=30)),
                ('supervisor_photo', models.FileField(upload_to='Assets/Files/Supervisor')),
            ],
        ),
    ]
